# EFF Rayhunter

`SUR-B3-13` · **90/100** · overall rank 40 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 12) |
| **Segment** | B3 · Protecting journalists and sources (rank 10) |
| **Subcategory** | Cell-site simulator detection |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Electronic Frontier Foundation |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/EFForg/rayhunter) · [Documentation](https://eff.org/rayhunter) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 90/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Rust application that runs on an inexpensive mobile hotspot to analyse the cellular control plane and detect behaviour characteristic of cell-site simulators (IMSI catchers), such as downgrade attacks and unusual identity requests.

## Journalism / investigative use case

Detecting whether a protest, a courthouse, a border crossing or a newsroom's surroundings are being surveilled with an IMSI catcher — a question journalists have had no practical way to answer, and one that is both a protective measure and, when a detection occurs, a story in itself.

## 2. Audience

specialist investigator, engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Addresses a surveillance technique that was effectively undetectable by journalists until now, and does so on hardware costing tens rather than thousands — a genuine capability change for the field
- Dual value: protective (know when your communications are being intercepted) and investigative (document that a specific location was surveilled at a specific time)
- GPL-3.0, very actively maintained (v0.13.0, 2026-09-16; pushed 2026-11-17) with 6,069 stars and EFF's institutional backing and legal literacy
- Runs on specific inexpensive hotspot hardware, so a newsroom can deploy several and build a picture over time

## 5. Cons

- Detections are heuristic signals about anomalous network behaviour, not proof that a cell-site simulator was present — and publishing 'an IMSI catcher was deployed' on a heuristic alone would be a serious overreach
- Requires specific supported hotspot hardware, and the supported-device list is a procurement constraint that varies by region and carrier bands
- Cellular-network behaviour varies legitimately by carrier and location, so baselining is necessary before anomalies mean anything — and that takes time and local knowledge
- GPL-3.0 and 6,069 stars indicate a young, rapidly developing project, so expect behaviour changes between versions and keep notes on which version produced which detection

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 6,069 stars with release v0.13.0 (2026-09-16) and a push on 2026-11-17, GPL-3.0, maintained by EFF. The rapid growth in stars for a hardware-dependent tool indicates substantial interest in the capability; EFF publishes guidance on interpreting results, which is the relevant support context.

## 7. Assessment

Adopt it — this is one of the most interesting items in the whole catalogue for your context, because it converts an invisible threat into something observable and reportable. Two disciplines are essential. First, baseline normal cellular behaviour in your locations before treating anomalies as detections, otherwise you will produce false alarms. Second, in published work describe what was observed (specific control-plane anomalies, at a time and place) rather than asserting the presence of a device, and get a cellular-security expert to review before publication. Deploy several units if protest or courthouse coverage is a regular beat.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v0.13.0 (2026-09-16), 6,069 stars, GPL-3.0. Same-day commits with frequent releases under EFF's institutional maintenance; a young project with strong momentum.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** GPL-3.0; immaterial for internal use. Note that operating cellular-monitoring equipment may engage local radio or wiretapping law — a legal question entirely separate from the licence, and one to check in each jurisdiction where you deploy.

**Licence evidence:** https://github.com/EFForg/rayhunter/blob/main/LICENSE

## 10. Costs

No software fee. Hardware: a supported mobile hotspot (low tens to low hundreds, estimate) per deployment plus a mobile data plan if you want it operating in the field. Among the best capability-per-cost items in the catalogue.

## 11. Privacy and data flows

Analysis is local on the device; nothing is transmitted to EFF. The data collected is about the network rather than about individuals, which keeps the privacy profile clean. Possession and operation of the device may itself attract attention in a hostile jurisdiction.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Requires specific supported hotspot hardware; operating cellular monitoring may engage local radio law

## 13. Alternatives

- Commercial IMSI-catcher detection products, which are expensive and opaque
- Crowdsourced cell-tower databases (OpenCellID) for corroborating anomalies against known infrastructure
- SnoopSnitch and similar Android apps, with narrower device support

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/EFForg/rayhunter
- https://eff.org/rayhunter
- https://github.com/EFForg/rayhunter/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Signal (Android client)](SUR-B3-23.md) | 95 | Adopt |
| 2 | [mat2](SUR-B3-07.md) | 94 | Adopt |
| 3 | [SecureDrop](SUR-B3-01.md) | 92 | Adopt |
| 4 | [CryptPad](SUR-B3-27.md) | 92 | Adopt |
| 5 | [Dangerzone](SUR-B3-03.md) | 92 | Adopt |
| 6 | [OnionShare](SUR-B3-04.md) | 92 | Adopt |
| 7 | [Orbot](SUR-B3-30.md) | 92 | Adopt |
| 8 | [Tails](SUR-B3-19.md) | 92 | Adopt |

---

← 39. [Buzz](JAI-A2-05.md) · 41. [OONI Explorer](SUR-B1-03.md) →
