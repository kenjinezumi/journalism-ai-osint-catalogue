# Internet Health Report (IHR)

`SUR-B1-13` · **74/100** · overall rank 225 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 59) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 18) |
| **Subcategory** | Network dependency analysis |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Internet Health Report project (IIJ Research Lab and collaborators) |
| **Maintenance** | Stable with low activity |
| **Licence** | GPL-3.0 |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/InternetHealthReport/ihr-website) · [Documentation](https://www.ihr.live/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 74/100**

---

## 1. Purpose

Platform computing and publishing per-AS and per-country internet health indicators — AS hegemony (transit dependency), delay and forwarding anomalies, link congestion — from public measurement and routing data.

## Journalism / investigative use case

Useful for the attribution half of a shutdown story: showing which upstream autonomous system a country depends on, and therefore which operator or transit provider is the chokepoint when connectivity drops. That turns 'the internet went down' into 'this specific operator was the single point of control'.

## 2. Audience

specialist investigator, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- AS hegemony is a genuinely distinctive metric for journalism: it identifies structural chokepoints, which is the precondition for a shutdown being technically possible
- Published as a browsable site plus an API, so a reporter can get the dependency picture without running the analysis
- GPL-3.0 with the front end actively released (v1.8.8, 2026-10-23)
- Combines routing and active-measurement data, so the indicators are not single-source

## 5. Cons

- A research codebase rather than a product: several analysis components (disco, ashash) have been untouched since 2022, so the pipeline behind the published indicators is unevenly maintained
- Indicators need expert interpretation — AS hegemony is a statistical dependency measure, not a statement that an operator controls traffic, and over-reading it would produce a wrong attribution in print
- Documentation is uneven, and the Kafka-based analysis stack is not realistically deployable by a newsroom
- Small community (93 stars) and the site is the only practical interface

## 6. Feedback (documented)

No individual user reports verified. Documented: the front end is actively released (v1.8.8, 2026-10-23) while named analysis components have been dormant since 2022 — a split maintenance picture verified from the project's repositories. 93 stars, 3 open issues.

## 7. Assessment

Use the published site and API for the structural question of who the chokepoints are; do not try to run the pipeline. For your profile the value is specific and real: when a shutdown happens, IHR tells you which operator to put the question to, which is the difference between reporting an outage and reporting a decision. Have the dependency interpretation checked by someone who understands BGP economics before attributing control to a named company.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: ihr-website archived=false, pushed_at 2026-10-23, latest release v1.8.8 same day, 93 stars, 3 open issues. However, sibling analysis components (disco, ashash) have not been updated since 2022 per session-1 inspection. Classified stable-low because the public service and front end are current while the analytical back end is partly frozen.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** Derived indicators are published on the site; data terms not separately verified in this survey.

**Restrictions:** GPL-3.0 on the website code; irrelevant for using the hosted service.

**Licence evidence:** https://github.com/InternetHealthReport/ihr-website/blob/master/LICENSE

## 10. Costs

Free to use. Self-hosting the full analysis would require RIPE Atlas and BGP data feeds plus a Kafka cluster — not a realistic newsroom cost, so no estimate is offered.

## 11. Privacy and data flows

Processes public network measurement and routing data into aggregate per-AS and per-country indicators; no end-user data is involved and browsing runs no measurement.

## 12. Verdict

**Integrate**

## 13. Alternatives

- PyBGPStream to compute dependency relationships yourself from public archives
- IODA for the outage event itself
- RIPEstat for simpler AS relationship lookups

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/InternetHealthReport/ihr-website
- https://www.ihr.live/
- https://github.com/InternetHealthReport/ihr-website/blob/master/LICENSE

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

← 224. [ICIJ Prophecies](OSINT-C3-08.md) · 226. [Leaflet](JAI-A1-21.md) →
