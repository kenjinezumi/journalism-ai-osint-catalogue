# OONI Probe CLI / probe-engine

`SUR-B1-01` · **85/100** · overall rank 81 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 26) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 4) |
| **Subcategory** | Censorship measurement |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Open Observatory of Network Interference (OONI) |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ooni/probe-cli) · [Documentation](https://ooni.org/support/ooni-probe-cli) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 5/5 · privacy 2/5 · usability 3/5 · licence+cost 4/5 → **weighted 85/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Command-line network-measurement client implementing OONI's test suite — web connectivity, instant-messaging apps, circumvention tools, performance — which uploads results to OONI's collector for publication as open data.

## Journalism / investigative use case

A reporter or local stringer runs ooniprobe from inside the affected country to generate timestamped, independently published evidence that specific news sites or messaging apps are being blocked, and what technique is doing the blocking (DNS tampering, TCP reset, TLS interference). That published measurement is citable in the story.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Produces third-party-verifiable evidence: because results are published to OONI's open dataset with a permalink, a story can cite the measurement rather than asserting a block
- Identifies the blocking technique, not just the fact of a block — which is what distinguishes a state-ordered DNS block from a site outage in print
- Very actively maintained (v3.31.1, 2026-11-03; pushed 2026-11-17) with institutional backing and a clean issue ratio
- GPL-3.0, cross-platform Go binaries, scriptable for repeated measurement over time

## 5. Cons

- Running probes is legally and physically risky for the operator in repressive jurisdictions — measurement traffic is distinguishable and the ASN and network name are published with the result, which can narrow down who ran it
- Results detect anomalies, not intent: confirming a block usually needs corroboration across probes, networks and time, and single measurements are routinely over-read
- Requires GeoIP databases and OONI's collector and test-helper infrastructure, so it is not a standalone tool
- Coverage is only what someone chose to test — a country can look unblocked because nobody ran a probe there

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: OONI's measurement corpus is used in published reporting and in advocacy submissions, and the project itself documents that results are published with ASN and network name — the key operational-security fact. 301 stars, 40 open issues, release 2026-11-03.

## 7. Assessment

Essential to this pillar and the thing I would reach for first on a 'is the site blocked' question — but the risk sits with the person running it, not with you. For media-in-exile work the responsible pattern is: never ask an in-country source to run a probe without explaining that the ASN and network are published; prefer existing OONI Explorer data where it already covers the network; and where you do commission measurement, corroborate across time and networks before publishing an attribution.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v3.31.1 (2026-11-03), 301 stars, 40 open issues. Frequent versioned releases, same-day commits, funded institutional maintainer with a security process.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** Published OONI measurement data is open data (CC0-style per OONI's policy — verify the current terms before bulk redistribution). The Citizen Lab test lists that drive testing are CC-BY-NC-SA-4.0, which is a separate and more restrictive licence.

**Restrictions:** GPL-3.0 on the client limits embedding in proprietary tooling. Note the test lists' NonCommercial clause if you redistribute them alongside results.

**Licence evidence:** https://github.com/ooni/probe-cli/blob/master/LICENSE.md

## 10. Costs

No fee. Negligible compute. The real cost is risk borne by the person running the probe, and the time to interpret results correctly.

## 11. Privacy and data flows

Measurement results are uploaded by default to OONI's collector and then published as open data including the probe's ASN, network name and country. This is deliberate — the value is public evidence — but it means the measurement is not private, and in a small network the ASN can be identifying. Treat running a probe as a public act.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Operator risk in repressive jurisdictions; ASN and network name are published with results

## 13. Alternatives

- [OONI Explorer](SUR-B1-03.md) first, to check whether existing measurements already answer the question without new risk
- RIPE Atlas tooling for reachability and routing measurement from volunteer probes
- IODA for country-level outage confirmation without in-country action

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ooni/probe-cli
- https://ooni.org/support/ooni-probe-cli
- https://github.com/ooni/probe-cli/blob/master/LICENSE.md

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [changedetection.io](SUR-B1-15.md) | 93 | Adopt |
| 2 | [OONI Explorer](SUR-B1-03.md) | 90 | Adopt |
| 3 | [IODA (Internet Outage Detection and Analysis)](SUR-B1-07.md) | 88 | Adopt |
| 5 | [OONI Probe Multiplatform](SUR-B1-02.md) | 85 | Adopt |
| 6 | [shot-scraper](SUR-B1-23.md) | 83 | Adopt |
| 7 | [webchanges](SUR-B1-17.md) | 82 | Adopt |
| 8 | [EDGI web-monitoring-diff](SUR-B1-21.md) | 81 | Integrate |
| 9 | [urlwatch](SUR-B1-16.md) | 80 | Integrate |

---

← 80. [meteostat](OSINT-C2-40.md) · 82. [adsb-history](OSINT-C2-48.md) →
