# PyBGPStream / libbgpstream

`SUR-B1-08` · **78/100** · overall rank 176 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 50) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 12) |
| **Subcategory** | Routing analysis |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | CAIDA (UC San Diego) |
| **Maintenance** | Stable with low activity |
| **Licence** | BSD-2-Clause |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/CAIDA/pybgpstream) · [Documentation](https://bgpstream.caida.org/docs) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 3/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 78/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | BSD-2-Clause |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | RouteViews and RIPE RIS MRT archives are public data under their respective providers' terms (not separately verified here). |
| **Restrictions** | None material for the code. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Infrastructure: compute and disk for MRT archive processing — a shutdown-window analysis is modest, a multi-month study is substantial. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/CAIDA/pybgpstream/blob/master/LICENSE
- https://github.com/CAIDA/pybgpstream
- https://bgpstream.caida.org/docs

---

## 1. Purpose

Python bindings over libBGPStream for streaming and analysing historical and near-real-time BGP routing data from RouteViews and RIPE RIS collectors.

## Journalism / investigative use case

Lets a data journalist independently reconstruct which ASNs withdrew which prefixes, and at what minute, during a shutdown — the evidence that distinguishes an operator-executed disconnection from a transit failure, and that survives a government's claim of a technical fault.

## 2. Audience

engineer, specialist investigator

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Gives you primary-source routing evidence rather than someone else's dashboard, which is what you need when a finding will be officially denied
- BSD-2-Clause, so the analysis code and methodology can be published alongside a story with no licence friction
- Reads public archives only — no probing, no user data, no risk to anyone in-country
- Minute-level granularity on route withdrawals is often the sharpest timestamp available for a shutdown

## 5. Cons

- Build and dependency setup is genuinely fiddly (libbgpstream, wandio, librdkafka C toolchain) and is where most people give up
- Release cadence is slow: last tagged release v2.0.4 in February 2024, with the last push 2026-07-06
- BGP shows control-plane intent: routes can remain announced while the data plane is blocked, so BGP silence proves disconnection but BGP presence does not prove connectivity
- Interpreting collector data correctly (peer visibility, prefix aggregation, collector outages) requires real expertise and is easy to get wrong in public

## 6. Feedback (documented)

No individual user reports verified. Documented: 45 stars with 22 open issues, last tagged release 2024-02-20, last push 2026-07-06. CAIDA's BGPStream is a standard instrument in network-measurement research, which is strong adjacent-field credibility.

## 7. Assessment

Worth the setup cost once, and then it is a durable capability: shutdown stories recur and this is the independent evidence layer. For your profile I would containerise it so the build pain is paid once, and pair it with IODA — IODA to find the event quickly, PyBGPStream to reconstruct it from primary data for publication. Have someone who understands BGP review the interpretation before it goes in print; the failure mode here is a confident wrong claim about which operator did what.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-07-06, latest release v2.0.4 (2024-02-20), 45 stars, 22 open issues. Four months since last push and over two years since a release; a mature research library with slow but non-zero maintenance under institutional ownership.

## 9. Licensing

**Licence:** BSD-2-Clause _(SPDX verified)_

**Model / data licence:** RouteViews and RIPE RIS MRT archives are public data under their respective providers' terms (not separately verified here).

**Restrictions:** None material for the code.

**Licence evidence:** https://github.com/CAIDA/pybgpstream/blob/master/LICENSE

## 10. Costs

No fee. Infrastructure: compute and disk for MRT archive processing — a shutdown-window analysis is modest, a multi-month study is substantial. Estimate.

## 11. Privacy and data flows

Reads public routing-table and update archives; no probing and no user data. One of the safest instruments in this pillar from an operational-security standpoint.

## 12. Verdict

**Integrate**

## 13. Alternatives

- IODA for a faster, no-setup answer — but academic licence on the code
- RIPE Atlas tooling for active reachability measurement alongside routing data
- RIPEstat APIs for simpler one-off routing lookups

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/CAIDA/pybgpstream
- https://bgpstream.caida.org/docs
- https://github.com/CAIDA/pybgpstream/blob/master/LICENSE

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

← 175. [PaddleOCR / PP-StructureV3](JAI-A2-37.md) · 177. [ThreatExchange (PDQ / TMK+PDQF / vPDQ and HMA)](OSINT-C2-06.md) →
