# RIPE Atlas tooling (Magellan CLI, Cousteau, Sagan)

`SUR-B1-12` · **75/100** · overall rank 204 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 57) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 16) |
| **Subcategory** | Active network measurement |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | RIPE NCC |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/RIPE-NCC/ripe-atlas-tools) · [Documentation](https://ripe-atlas-tools.readthedocs.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 3/5 · usability 3/5 · licence+cost 4/5 → **weighted 75/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Command-line client and Python libraries for scheduling and retrieving RIPE Atlas measurements — ping, traceroute, DNS, TLS, HTTP — from a global fleet of volunteer-hosted hardware probes.

## Journalism / investigative use case

Lets a reporter schedule pings, traceroutes, DNS and TLS measurements from probes inside a specific country or ASN during an unfolding shutdown, and watch probe disconnections as an independent outage signal — measurement from inside the affected network without asking any person there to act.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Measurement from inside the affected country without putting a human there at risk — the probes are already deployed, which is a significant ethical advantage over asking a source to run software
- Probe disconnection itself is a usable outage signal, independent of the measurements you schedule
- DNS and traceroute from in-country vantage points can distinguish DNS tampering from routing-level blocking, which is the technical detail a story needs
- Actively maintained (pushed 2026-10-22, tag v3.4.1) by RIPE NCC with a very clean issue tracker (10 open)

## 5. Cons

- Probe coverage is thin and skewed in exactly the countries that matter most for shutdown reporting — a country may have too few probes to support any claim, and this limitation is systematic rather than occasional
- The credit system is a real throttle on sustained measurement: you earn credits by hosting probes or receive an allowance, and heavy measurement exhausts it
- Results are by default published publicly in RIPE Atlas, so your measurement activity and targets are visible — an operational-security consideration if the target would object
- Release objects lag tags (v3.2.0 published 2025-09-25 against tag v3.4.1), and the CLI assumes familiarity with measurement concepts

## 6. Feedback (documented)

No individual user reports verified. Documented: the credit-system throttle and default public publication of results are stated in RIPE Atlas documentation; 218 stars with only 10 open issues, indicating good triage; last push 2026-10-22.

## 7. Assessment

The ethically cleanest way to measure from inside a hostile network, and for that reason the one I would reach for before commissioning an in-country OONI probe. Two practical cautions: check probe coverage for the target country before planning a story around it, because thin coverage will defeat you; and remember your measurements are public, so scheduling a burst of traceroutes at a government network is a visible act. Pair with PyBGPStream for the routing view.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-22, latest release v3.2.0 (2025-09-25), latest tag v3.4.1, 218 stars, 10 open issues. Low backlog and current commits under RIPE NCC institutional maintenance; release objects trail the tag line.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** RIPE Atlas measurement results are published under RIPE NCC's terms (not separately verified here).

**Restrictions:** GPL-3.0 on the tooling. Note that RIPE Atlas usage is governed by RIPE NCC's acceptable-use terms and the credit system, which are service conditions rather than licence terms.

**Licence evidence:** https://github.com/RIPE-NCC/ripe-atlas-tools/blob/master/LICENSE

## 10. Costs

No software fee. Measurement is throttled by RIPE Atlas credits: you earn them by hosting a probe or anchor, or receive a starting allowance. Sustained measurement realistically requires hosting probes — a hardware and bandwidth cost rather than a licence fee. Current credit rates were not verified in this survey.

## 11. Privacy and data flows

Measurements are initiated by you from third-party probes and, by default, results are published publicly in RIPE Atlas — so both your targets and your measurement pattern are visible. Probe hosts are volunteers whose networks are already exposed by participation; you are not adding risk to them, but you are acting visibly.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Thin probe coverage in many high-interest countries; measurements are public by default

## 13. Alternatives

- OONI Probe where application-layer blocking rather than reachability is the question
- PyBGPStream for the control-plane view with no measurement footprint
- IODA for a pre-computed outage answer

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/RIPE-NCC/ripe-atlas-tools
- https://ripe-atlas-tools.readthedocs.io/
- https://github.com/RIPE-NCC/ripe-atlas-tools/blob/master/LICENSE

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

← 203. [OWASP Amass](OSINT-C3-22.md) · 205. [uncover](OSINT-C1-10.md) →
