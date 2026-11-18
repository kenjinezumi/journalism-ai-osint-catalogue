# Alegre (Meedan)

`JAI-A4-02` · **63/100** · overall rank 302 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 114) |
| **Segment** | A4 · Fact-checking support and media verification (rank 7) |
| **Subcategory** | Similarity matching service |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Meedan |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/meedan/alegre) · [Documentation](https://github.com/meedan/alegre#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 4/5 · usability 2/5 · licence+cost 4/5 → **weighted 63/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Varies — bundles third-party sentence-transformer/BERT checkpoints whose own licences were NOT verified in this survey. |
| **Restrictions** | Code unrestricted; unresolved uncertainty at the bundled-model layer. Verify the specific checkpoints before commercial redistribution. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. Infrastructure: Elasticsearch/OpenSearch plus PostgreSQL plus model-serving containers; GPU helpful for embedding throughput. Optional Google Translate API charges if enabled (not priced here). Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/meedan/alegre/blob/master/LICENSE
- https://github.com/meedan/alegre

---

## 1. Purpose

Multilingual and multimodal similarity service exposing text, image, audio and video similarity search over a vector index, used as the matching engine behind Meedan Check.

## Journalism / investigative use case

Powers tipline and fact-check deduplication at scale: when a reader submits an image or claim, Alegre finds whether a near-identical item has already been received and checked, so the desk answers from existing work instead of re-verifying. At high tipline volume this is the difference between a functioning service and a backlog.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Multimodal in one service — text, image, audio and video similarity — which is otherwise four separate integrations
- Self-hostable, so media and hashes stay on infrastructure you control; important because tipline media is often sensitive
- MIT licensed with an active tag cadence (v0.187.2) and real production use behind Check
- Solves a specific, measurable problem (duplicate workload) rather than promising verification

## 5. Cons

- Similarity answers 'have we seen this before?', not 'is this real?' — it provides no synthetic-media or manipulation detection, and conflating the two is a serious misreading
- Bundles third-party sentence-transformer and BERT checkpoints whose own licences were not verified in this survey — a real gap for commercial redistribution
- Requires Elasticsearch/OpenSearch, PostgreSQL and Docker; optional Google Translate integration sends text off-box
- Tiny external community (15 stars, 22 open issues) and no GitHub release objects — effectively a Meedan internal service published openly, so self-hosting support is limited

## 6. Feedback (documented)

No individual user reports verified. Production evidence is structural: Alegre is the matching layer of Meedan Check, which is deployed by fact-checking partners. The unverified bundled-model licences are an explicit gap carried into this entry rather than resolved.

## 7. Assessment

Worth running only as part of a Check deployment or where you specifically need multimodal near-duplicate matching at volume. For your profile a lighter alternative — ImageHash plus a sentence-transformers index — gives you most of the capability with components you control and whose licences you can verify. Alegre's advantage is that it is already integrated and battle-tested; its disadvantage is opacity about the models inside it.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-09-28, latest tag v0.187.2, no GitHub release objects, 15 stars, 22 open issues. Continuous versioned tagging driven by Check's needs; maintenance is institutional rather than community-driven.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Varies — bundles third-party sentence-transformer/BERT checkpoints whose own licences were NOT verified in this survey.

**Restrictions:** Code unrestricted; unresolved uncertainty at the bundled-model layer. Verify the specific checkpoints before commercial redistribution.

**Licence evidence:** https://github.com/meedan/alegre/blob/master/LICENSE

## 10. Costs

No fee. Infrastructure: Elasticsearch/OpenSearch plus PostgreSQL plus model-serving containers; GPU helpful for embedding throughput. Optional Google Translate API charges if enabled (not priced here). Estimate.

## 11. Privacy and data flows

Self-hostable so media and hashes remain yours. Optional translation and LLM integrations send text to third parties if configured — review before enabling, since tipline text can identify a submitter.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [ImageHash](OSINT-C2-05.md) plus sentence-transformers for a self-assembled, licence-verifiable equivalent
- ThreatExchange PDQ/vPDQ for standards-based perceptual hashing of images and video
- [Meedan Check](JAI-A4-01.md), which bundles Alegre and is the usual reason to run it

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/meedan/alegre
- https://github.com/meedan/alegre/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [x-ray](JAI-A4-23.md) | 91 | Adopt |
| 2 | [InVID-WeVerify Verification Plugin](JAI-A4-04.md) | 82 | Adopt |
| 3 | [Meedan Check](JAI-A4-01.md) | 80 | Pilot |
| 4 | [CooRTweet](JAI-A4-13.md) | 77 | Adopt |
| 5 | [kuroi](JAI-A4-24.md) | 71 | Pilot |
| 6 | [Community Forensics](JAI-A4-21.md) | 65 | Pilot |
| 8 | [CAT-Net](JAI-A4-19.md) | 63 | Pilot |
| 9 | [TruFor](JAI-A4-18.md) | 61 | Monitor |

---

← 301. [SpiderFoot](OSINT-C3-29.md) · 303. [CAT-Net](JAI-A4-19.md) →
