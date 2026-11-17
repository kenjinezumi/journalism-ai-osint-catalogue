# M-Lab NDT server, ndt7 client and MSAK

`SUR-B1-11` · **74/100** · overall rank 232 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 60) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 19) |
| **Subcategory** | Network performance measurement |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Measurement Lab (M-Lab) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/m-lab/ndt-server) · [Documentation](https://www.measurementlab.net/tests/ndt/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 3/5 · usability 3/5 · licence+cost 5/5 → **weighted 74/100**

---

## 1. Purpose

Open server and client implementations of the Network Diagnostic Tool (ndt7) and the multi-stream MSAK test, plus the published M-Lab dataset of billions of throughput measurements.

## Journalism / investigative use case

Evidence for throttling and degradation stories — the slow-lane variant of a shutdown, where connectivity technically persists but collapses in throughput — and for long-run comparisons of network performance by ISP and region, which is how you show that a specific provider degraded a specific service.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- The published M-Lab dataset is an enormous longitudinal record of real client measurements, which makes before-and-after throttling claims quantifiable rather than anecdotal
- Apache-2.0 across the stack with the server runnable yourself if you want controlled measurements from known vantage points
- Active maintenance (v0.26.1 released 2026-10-15, same-day push) under a long-standing institutional programme
- Open data publication model means your analysis can be reproduced by a reader or a regulator

## 5. Cons

- This is performance measurement, not censorship detection: it will not tell you a site is blocked, only that a path is degraded, and attributing degradation to deliberate throttling needs corroboration you must supply
- M-Lab publishes results openly including truncated client IP and ASN — a documented and deliberate design choice, but it means measurements are not private and a client on a small network may be identifiable
- 88 open issues and a multi-repository ecosystem (server, clients, MSAK, data pipelines) that takes orientation effort
- Throughput measurement is noisy: client-side conditions (wifi, device, congestion) confound ISP-level conclusions, so single tests prove nothing

## 6. Feedback (documented)

No individual user reports verified. Documented: the open publication of results including truncated client IP and ASN is stated by M-Lab; 137 stars with 88 open issues; release v0.26.1 on 2026-10-15. M-Lab data has been used in regulatory and journalistic analysis of broadband performance, which is credible usage context.

## 7. Assessment

Useful for a specific and under-covered story type — throttling rather than blocking — where it is close to the only open evidence source. For your profile the realistic use is analysing the published dataset rather than running servers: pull per-ASN throughput time series around a disputed event and look for the discontinuity. Be rigorous about confounders, and be aware that encouraging readers to run tests produces measurements published with their truncated IP and ASN.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-15, latest release v0.26.1 published the same day, 137 stars, 88 open issues. Regular releases under a funded institutional programme with an operating server fleet.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** M-Lab publishes its measurement dataset openly (CC-BY-style per M-Lab's data policy — verify current terms before bulk redistribution).

**Restrictions:** None material for the code.

**Licence evidence:** https://github.com/m-lab/ndt-server/blob/main/LICENSE

## 10. Costs

No fee. Analysing the published dataset via BigQuery incurs Google Cloud query charges (usage-based; current rates not verified here). Running your own NDT server is a modest VM plus bandwidth. Estimate.

## 11. Privacy and data flows

Tests measure the client's own connection, and M-Lab publishes results openly including truncated client IP and ASN — a documented trade-off in favour of open data. Anyone you ask to run a test should be told their network is published. Querying the dataset exposes your analysis interest to Google.

## 12. Verdict

**Integrate**

## 13. Alternatives

- OONI for blocking rather than degradation
- RIPE Atlas for latency and reachability from fixed vantage points
- Cloudflare Radar or ISP-published data for corroboration, with their own terms

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/m-lab/ndt-server
- https://www.measurementlab.net/tests/ndt/
- https://github.com/m-lab/ndt-server/blob/main/LICENSE

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

← 231. [LangGraph](JAI-A3-10.md) · 233. [Unstructured](JAI-A1-10.md) →
