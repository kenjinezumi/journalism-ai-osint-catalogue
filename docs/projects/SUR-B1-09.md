# Censored Planet data analysis pipeline

`SUR-B1-09` · **76/100** · overall rank 197 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 53) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 13) |
| **Subcategory** | Censorship measurement |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Censored Planet (University of Michigan) |
| **Maintenance** | Stable with low activity |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/censoredplanet/censoredplanet-analysis) · [Documentation](https://censoredplanet.org/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 3/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 76/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Published Censored Planet data terms were not separately verified in this survey; check before bulk redistribution. |
| **Restrictions** | Code permissive. Data terms unverified here. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No software fee. Querying the published BigQuery tables incurs Google Cloud charges based on bytes scanned — a real, usage-based cost that scales with how broadly you query (current BigQuery rates not verified in this survey). Raw data releases can be downloaded instead, trading cloud cost for storage and compute.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/censoredplanet/censoredplanet-analysis/blob/master/LICENSE
- https://github.com/censoredplanet/censoredplanet-analysis
- https://censoredplanet.org/

---

## 1. Purpose

Pipeline that processes Censored Planet's raw remote-measurement data (Hyperquack, Satellite/Iris) into analysis tables published in BigQuery, covering network interference across roughly 200 countries without in-country probes.

## Journalism / investigative use case

Underpins global, longitudinal blocking comparisons across around 200 countries without anyone having to run a probe inside a censored network — which matters precisely when in-country testing would be unsafe for the person doing it.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Remote measurement removes operator risk entirely, making it the ethically preferable source when you cannot ask anyone in-country to take a risk
- Global and longitudinal by design, so cross-country comparisons are methodologically consistent rather than assembled from disparate sources
- Apache-2.0 with published BigQuery tables, so the analytical deliverable is directly queryable
- Academic provenance with published methodology, so findings can be defended and cited

## 5. Cons

- Not runnable by a newsroom in practice — it is a GCP-based pipeline over data you do not hold; treat the published BigQuery tables and raw releases as the deliverable and this repository as methodological documentation
- Remote-measurement techniques infer blocking from outside the network, so they are weaker than in-country measurement on some interference types and carry their own false-positive modes
- Last push 2025-06-29 with no releases and 20 stars — the pipeline repository is lightly maintained even while the data programme continues
- Using the BigQuery tables means a Google Cloud account and query costs, which is a paid dependency

## 6. Feedback (documented)

No individual user reports verified. Documented: last push 2025-06-29, no releases, 20 stars, 13 open issues; Apache-2.0; dependency on GCP and on censoredplanet/assets-censoredplanet for blockpage fingerprints. Censored Planet's published research is well established in the measurement literature.

## 7. Assessment

Use the published data, not the code. For your profile the decisive advantage over OONI is ethical rather than technical: it answers blocking questions without putting a person in a hostile jurisdiction at risk, which should make it your first option when the alternative is asking a source to run a probe. Budget for BigQuery query costs and have a methodologist check the inference limits before you publish a country comparison.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2025-06-29, no releases or tags, 20 stars, 13 open issues. Seventeen months since last push. The research programme and data publication continue, so the pipeline code is stable rather than abandoned — but the repository alone is weak evidence either way, hence the cautious classification.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** Published Censored Planet data terms were not separately verified in this survey; check before bulk redistribution.

**Restrictions:** Code permissive. Data terms unverified here.

**Licence evidence:** https://github.com/censoredplanet/censoredplanet-analysis/blob/master/LICENSE

## 10. Costs

No software fee. Querying the published BigQuery tables incurs Google Cloud charges based on bytes scanned — a real, usage-based cost that scales with how broadly you query (current BigQuery rates not verified in this survey). Raw data releases can be downloaded instead, trading cloud cost for storage and compute.

## 11. Privacy and data flows

Processes already-published remote-measurement data about network behaviour. The measurement technique probes infrastructure from outside, so no individual in-country is involved or exposed. Your BigQuery queries are visible to Google.

## 12. Verdict

**Integrate**

## 13. Alternatives

- OONI data where in-country measurement exists and is safe
- IODA for outage rather than blocking questions
- [CenAlert](SUR-B1-10.md) for early-warning signals derived partly from this data

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/censoredplanet/censoredplanet-analysis
- https://censoredplanet.org/
- https://github.com/censoredplanet/censoredplanet-analysis/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [changedetection.io](SUR-B1-15.md) | 93 | Adopt |
| 2 | [OONI Explorer](SUR-B1-03.md) | 90 | Adopt |
| 3 | [IODA (Internet Outage Detection and Analysis)](SUR-B1-07.md) | 88 | Adopt |
| 4 | [OONI Probe CLI / probe-engine](SUR-B1-01.md) | 85 | Adopt |
| 5 | [OONI Probe Multiplatform](SUR-B1-02.md) | 85 | Adopt |
| 6 | [shot-scraper](SUR-B1-23.md) | 83 | Adopt |
| 7 | [webchanges](SUR-B1-17.md) | 82 | Adopt |
| 8 | [EDGI web-monitoring-diff](SUR-B1-21.md) | 81 | Integrate |

---

← 196. [Amnesty International investigations (indicators of compromise)](SUR-B3-11.md) · 198. [OONI Data (oonidata / oonipipeline)](SUR-B1-05.md) →
