# mitmproxy

`SUR-B2-06` · **96/100** · overall rank 3 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 1) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 1) |
| **Subcategory** | Network traffic interception |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | mitmproxy project |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/mitmproxy/mitmproxy) · [Documentation](https://docs.mitmproxy.org/) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 96/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Interactive TLS-capable intercepting HTTP(S) proxy with a console UI, web interface and Python scripting API, allowing inspection, modification and recording of traffic.

## Journalism / investigative use case

Showing what an app or device actually sends and to whom: put a phone behind mitmproxy, use the app, and record the endpoints, payloads and identifiers transmitted. 'This app sent your contacts to this company's servers' is a story; 'this app requests contacts permission' is not.

## 2. Audience

engineer, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Observed transmission is the strongest form of evidence in app and device investigation — it documents conduct rather than capability, and that is what makes a publishable claim
- Python scripting API means you can automate capture and extraction across many apps or repeated sessions, turning a one-off demonstration into a survey
- MIT licensed with outstanding maintenance (v12.3.1, 2026-10-25; pushed 2026-11-14) and a very large community (47,047 stars)
- Local and self-contained: no cloud service, so the traffic you capture stays with you

## 5. Cons

- Requires installing a CA certificate on the device under test, which modern Android and iOS increasingly resist, and many apps use certificate pinning that defeats interception without further work (patching the app, which escalates the legal question)
- Captured traffic contains credentials, tokens and personal data of whoever used the device — treat captures as highly sensitive and keep them briefly
- Interception of a device you do not own, or of someone else's traffic, raises serious legal and ethical issues; this must be your own test device
- 560 open issues reflecting a broad feature surface; the learning curve for scripting is real

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 47,047 stars with 560 open issues, release v12.3.1 (2026-10-25), pushed 2026-11-14, MIT licence. mitmproxy is the standard tool for HTTP interception across security and development work, which is well established in its own documentation and ecosystem.

## 7. Assessment

Adopt it — the capability to show what an app transmits is the single most valuable technical input to surveillance-industry reporting, and nothing else does it as well. For your profile the operating rules are: use a dedicated test device you own, never intercept a colleague's or source's live traffic, destroy captures promptly because they contain credentials, and expect certificate pinning to block the most interesting apps, at which point the realistic options are a specialist partner or a rooted test device with the legal position checked.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-14, latest release v12.3.1 (2026-10-25), 47,047 stars, 560 open issues. Frequent releases on a 12.x line with a broad contributor base and long-term stability.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material. The constraints are legal rather than licensing: intercepting traffic you are not authorised to intercept is unlawful in most jurisdictions.

**Licence evidence:** https://github.com/mitmproxy/mitmproxy/blob/main/LICENSE

## 10. Costs

No fee. A test device and a workstation; negligible infrastructure.

## 11. Privacy and data flows

All capture is local. The sensitivity runs the other way: captures contain credentials and personal data from the test session, so storage, access and retention need the same care as source material.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Certificate pinning blocks interception for many apps; intercepting traffic you are not authorised to intercept is unlawful

## 13. Alternatives

- MobSF's dynamic analysis, which wraps interception into an app-analysis workflow
- Wireshark for lower-level packet capture where HTTP is not the layer of interest
- Frida for defeating certificate pinning — which escalates the legal and technical commitment

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/mitmproxy/mitmproxy
- https://docs.mitmproxy.org/
- https://github.com/mitmproxy/mitmproxy/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 2 | [MobSF (Mobile Security Framework)](SUR-B2-04.md) | 88 | Adopt |
| 3 | [Citizen Lab publication directory](SUR-B2-20.md) | 86 | Reference only |
| 4 | [Exodus Privacy](SUR-B2-01.md) | 86 | Adopt |
| 5 | [USAspending.gov (custom award data)](SUR-B2-14.md) | 86 | Adopt |
| 6 | [Apktool](SUR-B2-05.md) | 86 | Adopt |
| 7 | [TED — Tenders Electronic Daily (EU public procurement)](SUR-B2-13.md) | 84 | Adopt |
| 8 | [DuckDuckGo Tracker Radar](SUR-B2-03.md) | 82 | Reference only |
| 9 | [Blacklight collector](SUR-B2-02.md) | 81 | Adopt |

---

← 2. [llama.cpp](JAI-A3-01.md) · 4. [Scrapy](OSINT-C1-16.md) →
