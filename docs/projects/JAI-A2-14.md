# entity-fishing

`JAI-A2-14` · **68/100** · overall rank 279 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 108) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 57) |
| **Subcategory** | Entity linking |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Patrice Lopez (kermitt2) / Science-Miner |
| **Maintenance** | Stable with low activity |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/kermitt2/entity-fishing) · [Documentation](https://nerd.readthedocs.io/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 68/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Ships its own models and knowledge-base builds. The knowledge base derives from Wikidata (CC0) and Wikipedia (CC-BY-SA) — the CC-BY-SA component is worth noting if you redistribute a derived knowledge base. |
| **Restrictions** | Code permissive. Derived knowledge bases inherit Wikipedia's CC-BY-SA obligations if redistributed. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. Costs are storage (tens of GB for the knowledge base) and a JVM service with several GB of RAM, plus the engineer time to build and periodically rebuild the KB. Infrastructure estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/kermitt2/entity-fishing/blob/master/LICENSE
- https://github.com/kermitt2/entity-fishing
- https://nerd.readthedocs.io/

---

## 1. Purpose

Entity recognition and disambiguation service that links text mentions to Wikidata QIDs using an LMDB-backed knowledge base built from Wikidata and Wikipedia dumps, exposed as a REST API.

## Journalism / investigative use case

Resolving ambiguous names in a document set to stable identifiers so the same politician spelled three different ways across a leak collapses into one node — the prerequisite for building a reliable entity graph from messy text, and all of it offline.

## 2. Audience

engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Fully local entity linking after the knowledge base is built — a genuine and rare advantage over hosted linking APIs when the documents cannot leave your network
- Wikidata QIDs are stable, language-independent identifiers, which makes cross-language and cross-dataset joins possible in a way raw NER strings never allow
- Multilingual and designed for scale, with a REST interface that drops into any pipeline
- Apache-2.0 with the project shipping its own models and knowledge-base builds

## 5. Cons

- Heavy install and a large disk footprint for the LMDB knowledge base — a real operational commitment, not a pip install
- The knowledge base goes stale unless you rebuild it from new dumps, and rebuilding is itself a substantial batch job
- Coverage is limited to entities that exist in Wikidata, which excludes most shell companies, private individuals and local officials — precisely the entities investigations care about most
- No GitHub release objects (latest tag 0.0.6) and 49 open issues against 270 stars; essentially a specialist research tool with a thin community

## 6. Feedback (documented)

No user reports collected. Documented context: same maintainer as GROBID, which has a strong reputation in scholarly document processing — relevant as a credibility signal for engineering quality, not as evidence of newsroom use. No journalism deployment verified.

## 7. Assessment

Valuable but narrow, and the Wikidata-coverage limit is the decisive constraint for investigative work: it will confidently link the minister and silently miss the shell company. For your profile I would use it where the subject matter is public figures and institutions (political reporting, procurement, academia) and not expect it to help on a corporate-ownership leak. Budget a day for the knowledge-base build and a recurring job to refresh it.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-08-05, latest tag 0.0.6, no release objects, 270 stars, 49 open issues. Commits within the last four months and no deprecation notice, but low velocity and informal versioning. Classified stable-low rather than declining because the maintainer remains active across related projects (GROBID) and the tool is functionally complete.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** Ships its own models and knowledge-base builds. The knowledge base derives from Wikidata (CC0) and Wikipedia (CC-BY-SA) — the CC-BY-SA component is worth noting if you redistribute a derived knowledge base.

**Restrictions:** Code permissive. Derived knowledge bases inherit Wikipedia's CC-BY-SA obligations if redistributed.

**Licence evidence:** https://github.com/kermitt2/entity-fishing/blob/master/LICENSE

## 10. Costs

No fee. Costs are storage (tens of GB for the knowledge base) and a JVM service with several GB of RAM, plus the engineer time to build and periodically rebuild the KB. Infrastructure estimate.

## 11. Privacy and data flows

Fully local once the knowledge base is built; no document text leaves the machine. This is its main argument over cloud entity-linking APIs, which see every document you process.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [spaCy](JAI-A2-47.md) or GLiNER plus your own gazetteer where targets are known in advance
- [nomenklatura](JAI-A2-30.md) with FollowTheMoney for entity resolution over structured records
- [OpenRefine](JAI-A2-36.md) reconciliation against a self-hosted yente instance — but note reconciliation leaks values if pointed at a public service

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/kermitt2/entity-fishing
- https://nerd.readthedocs.io/
- https://github.com/kermitt2/entity-fishing/blob/master/LICENSE

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

← 278. [4get](OSINT-C1-02.md) · 280. [GlotLID](JAI-A2-20.md) →
