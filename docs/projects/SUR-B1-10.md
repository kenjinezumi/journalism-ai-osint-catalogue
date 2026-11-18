# CenAlert

`SUR-B1-10` · **54/100** · overall rank 337 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 77) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 25) |
| **Subcategory** | Censorship early warning |
| **Type** | prototype |
| **Bucket** | `verified-oss` |
| **Maintainer** | Censored Planet (University of Michigan) |
| **Maintenance** | Stable with low activity |
| **Licence** | GPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/censoredplanet/cenalert) · [Documentation](https://censoredplanet.org/) |

**Scores** — relevance 3/5 · capability 2/5 · maintenance 3/5 · privacy 3/5 · usability 1/5 · licence+cost 4/5 → **weighted 54/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | GPL-3.0 limits embedding in proprietary tooling; irrelevant for internal use. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. Requires Google Trends access (terms and rate limits outside your control; not priced here) and a Slack workspace. Minimal compute.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/censoredplanet/cenalert/blob/main/LICENSE
- https://github.com/censoredplanet/cenalert

---

## 1. Purpose

Research prototype that combines aggregate public search-interest signals with censorship-measurement data to raise early alerts that a country may have begun censoring a topic, pushing notifications to Slack.

## Journalism / investigative use case

Points toward an early-warning tripwire — being told a country may have started censoring a topic before a story breaks — rather than confirming a block after the fact. For an exile outlet, early notice that your own topic area is being filtered is operationally valuable.

## 2. Audience

engineer, specialist investigator

## 3. Project type

prototype · bucket `verified-oss`

## 4. Pros

- Addresses the right problem: existing tools confirm censorship retrospectively, and the newsworthy moment is when it starts
- GPL-3.0 and recently active (pushed 2026-11-17), so the approach is inspectable and current
- Architecturally simple — configuration plus a Slack webhook — so the concept is cheap to reimplement if the prototype does not suit

## 5. Cons

- A paper-accompanying prototype with almost no external users (3 stars), thin documentation and no packaging — this is research code, not a tool
- Alerts are probabilistic hints that must be verified against OONI or IODA before publication; an alert alone is not a finding
- Requires Google Trends access, a Slack token and per-topic/per-country configuration in a shell script — brittle, and Google Trends access terms and stability are outside your control
- Narrow Python version support (3.8-3.12) and no release engineering

## 6. Feedback (documented)

No individual user reports verified — 3 stars means there is no community signal, which I note rather than inflate. The approach is published research from a credible measurement group; the implementation is a prototype by the project's own framing.

## 7. Assessment

Take the idea, not the code. The concept — correlate a drop in search interest or a measurement anomaly with a topic you care about and get alerted — is worth building properly for the countries your outlet covers, and it is a few days of work against the OONI API plus a simple baseline. CenAlert's value to you is as a published method and a Slack-alert pattern. Any alert must be corroborated before it informs reporting.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, no releases or tags, 3 stars, 0 open issues. Current commits from the research group but no packaging, documentation maturity or community. Classified stable-low: active hands, prototype status.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** GPL-3.0 limits embedding in proprietary tooling; irrelevant for internal use.

**Licence evidence:** https://github.com/censoredplanet/cenalert/blob/main/LICENSE

## 10. Costs

No fee. Requires Google Trends access (terms and rate limits outside your control; not priced here) and a Slack workspace. Minimal compute.

## 11. Privacy and data flows

Consumes aggregate public search-interest signals and censorship-measurement data and pushes alerts to a Slack workspace. No individual data; note that your topic and country configuration reveals your editorial interests to Google Trends and to Slack.

## 12. Verdict

**Monitor**

## 13. Alternatives

- A custom alerting job against the OONI measurements API for the domains you care about
- IODA's own alerting for outage-level events
- Censored Planet BigQuery tables with a scheduled query and threshold

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/censoredplanet/cenalert
- https://github.com/censoredplanet/cenalert/blob/main/LICENSE

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

← 336. [Zingg](JAI-A1-20.md) · 338. [wpull](OSINT-C1-25.md) →
