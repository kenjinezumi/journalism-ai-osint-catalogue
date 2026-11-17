# IODA (Internet Outage Detection and Analysis)

`SUR-B1-07` · **88/100** · overall rank 50 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 15) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 3) |
| **Subcategory** | Outage detection |
| **Type** | platform |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | Georgia Tech InetIntel (previously CAIDA) |
| **Maintenance** | Actively maintained |
| **Licence** | NOT OSS — academic research and education use without fee; other uses directed to contact the university (LICENSE text read on both the CAIDA and InetIntel copies) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/InetIntel/ioda-ui) · [Documentation](https://ioda.inetintel.cc.gatech.edu/) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 4/5 · privacy 4/5 · usability 5/5 · licence+cost 2/5 → **weighted 88/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

System that detects and visualises internet outages by combining three independent signals — BGP routing withdrawals, active ICMP probing of address space, and background radiation observed at a network telescope — at country, region and ASN granularity.

## Journalism / investigative use case

The standard first stop for confirming and timestamping a national or regional internet shutdown, because agreement across three unrelated signals is hard to explain away as a measurement artefact — which is exactly the standard a shutdown story needs to survive official denial.

## 2. Audience

journalist, specialist investigator, newsroom analyst

## 3. Project type

platform · bucket `source-available-restricted`

## 4. Pros

- Triangulation across three independent signal types is the methodological strength: a shutdown visible in BGP, active probing and telescope data simultaneously is very strong evidence
- Country and ASN granularity lets you say which operator went dark and when, which is the attribution-relevant detail
- Hosted dashboard requires no technical skill and no in-country action, so there is no risk to anyone
- Actively operated (pushed 2026-11-16) with institutional backing at Georgia Tech

## 5. Cons

- The LICENSE text read on both the CAIDA and InetIntel copies grants use for academic research and education without fee and directs other uses to contact the university — so despite public code this is NOT open source for a commercial newsroom
- Release objects are stale (v1.0.0 from 2024-02-21) and the repository has 59 open issues with only 3 stars — the hosted service is the real artefact and the code is hard to assess
- Measures reachability, not cause: it shows that address space became unreachable, not who ordered it or why — attribution remains reporting work
- Self-hosting is impractical: it requires BGP collector feeds, probeable address space and a darknet telescope, which no newsroom has

## 6. Feedback (documented)

No individual user reports verified. Documented: the academic-research-and-education licence text read on both the CAIDA and InetIntel copies (verified session 1, retained); 59 open issues; v1.0.0 release from February 2024. IODA is widely cited in shutdown reporting and advocacy, which is credible usage evidence for the hosted dashboard.

## 7. Assessment

Use the hosted dashboard freely for confirming and timestamping shutdowns — that is its purpose and it is excellent at it. Do not plan to self-host or to build a product on the code, because the licence directs non-academic use to the university. For your profile the practical combination on a shutdown story is IODA for the timestamp and the affected ASNs, PyBGPStream for independently reconstructing the route withdrawals, and OONI for what was blocked rather than merely unreachable.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v1.0.0 (2024-02-21), SPDX NOASSERTION (actual: academic-use licence), 3 stars, 59 open issues. The hosted service is continuously operated and the UI repository receives current commits; institutional maintenance at Georgia Tech.

## 9. Licensing

**Licence:** NOT OSS — academic research and education use without fee; other uses directed to contact the university (LICENSE text read on both the CAIDA and InetIntel copies) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Published IODA data terms were not separately verified in this survey.

**Restrictions:** Commercial use of the code requires contacting the university. Using the public dashboard and citing it in reporting is ordinary use of a public service; redistributing the code or data commercially is not covered.

**Licence evidence:** https://github.com/InetIntel/ioda-ui

## 10. Costs

Free to use the dashboard. Self-hosting is impractical (BGP feeds, probeable address space, a network telescope). No realistic infrastructure estimate because the architecture is not reproducible by a newsroom.

## 11. Privacy and data flows

Aggregates network-level public measurement data to country, region and ASN granularity; it observes reachability of address space rather than individuals. Using the dashboard runs no measurement from your machine and exposes no one in-country.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Academic-use licence on the code — not usable as commercial newsroom infrastructure (the public dashboard is fine to use and cite)

## 13. Alternatives

- PyBGPStream to independently reconstruct BGP withdrawals from public archives
- [OONI Explorer](SUR-B1-03.md) for what was blocked rather than unreachable
- [Internet Society Pulse](SUR-B1-14.md) or Cloudflare Radar for quick summary figures, with their own terms

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `repo-inspected`

- https://github.com/InetIntel/ioda-ui
- https://ioda.inetintel.cc.gatech.edu/

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [changedetection.io](SUR-B1-15.md) | 93 | Adopt |
| 2 | [OONI Explorer](SUR-B1-03.md) | 90 | Adopt |
| 4 | [OONI Probe CLI / probe-engine](SUR-B1-01.md) | 85 | Adopt |
| 5 | [OONI Probe Multiplatform](SUR-B1-02.md) | 85 | Adopt |
| 6 | [shot-scraper](SUR-B1-23.md) | 83 | Adopt |
| 7 | [webchanges](SUR-B1-17.md) | 82 | Adopt |
| 8 | [EDGI web-monitoring-diff](SUR-B1-21.md) | 81 | Integrate |
| 9 | [urlwatch](SUR-B1-16.md) | 80 | Integrate |

---

← 49. [Playwright](JAI-A1-08.md) · 51. [WhisperX](JAI-A2-60.md) →
