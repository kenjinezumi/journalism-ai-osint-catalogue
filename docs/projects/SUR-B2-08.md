# WhatWeb

`SUR-B2-08` · **64/100** · overall rank 298 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 72) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 18) |
| **Subcategory** | Technology fingerprinting |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Andrew Horton (urbanadventurer) and Brendan Coles |
| **Maintenance** | Stable with low activity |
| **Licence** | GPL-2.0 (project licensing — confirm from the repository licence file for your records) |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/urbanadventurer/WhatWeb) · [Documentation](https://github.com/urbanadventurer/WhatWeb#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 3/5 · usability 4/5 · licence+cost 4/5 → **weighted 64/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-2.0 (project licensing — confirm from the repository licence file for your records) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | GPL-family copyleft on the tool; immaterial for internal use. Active scanning may engage computer-misuse law depending on jurisdiction and target — a legal rather than licence question. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. Ruby runtime; negligible resources.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/urbanadventurer/WhatWeb

---

## 1. Purpose

Web technology fingerprinting scanner with over a thousand plugins that identifies content management systems, frameworks, analytics, server software and embedded devices, with configurable aggression levels.

## Journalism / investigative use case

Fingerprinting a target's web infrastructure in one command: identify the CMS and server stack of a surveillance vendor's site, or sweep a list of suspected front organisations to find which share an unusual platform. The device-detection plugins also identify exposed appliances, which matters when mapping surveillance infrastructure.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Self-contained CLI with its own plugin database, so unlike webappanalyzer you get results immediately with no engine to build
- Aggression levels let you choose between passive identification and active probing, which is both an accuracy and an operational-security control
- Identifies embedded devices and appliances as well as web stacks, useful when the subject is physical surveillance infrastructure exposed to the internet
- Long-established tool packaged in security distributions, so it is available and familiar

## 5. Cons

- Active scanning modes send probes that are detectable and may be logged as hostile by the target — an operational-security and potentially legal consideration when the target is a surveillance company
- Ruby-based with a plugin architecture of considerable age; maintenance is steady rather than brisk and the plugin database ages against modern JavaScript-heavy sites
- Fingerprints are inferences and produce false positives, so an attribution based on a single match is weak
- Security-tooling heritage means the defaults and documentation assume penetration-testing context rather than journalism

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived with a substantial history; maintenance is steady rather than frequent. WhatWeb's standing as a fingerprinting tool is established by its inclusion in standard security distributions.

## 7. Assessment

Keep it for quick reconnaissance, with the aggression level set low when the target would object to being probed. For your profile the practical pairing is WhatWeb for a first pass and certificate-transparency plus registry data for attribution, because fingerprint matches alone will not survive a challenge. Treat scanning a surveillance vendor's infrastructure as a visible act and route it through an egress that is not your newsroom.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived. A mature Ruby tool with a long release history and steady rather than frequent updates; the plugin database is the component that matters and it ages gradually against modern sites.

## 9. Licensing

**Licence:** GPL-2.0 (project licensing — confirm from the repository licence file for your records) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** GPL-family copyleft on the tool; immaterial for internal use. Active scanning may engage computer-misuse law depending on jurisdiction and target — a legal rather than licence question.

**Licence evidence:** https://github.com/urbanadventurer/WhatWeb

## 10. Costs

No fee. Ruby runtime; negligible resources.

## 11. Privacy and data flows

Scanning is visible to the target. Passive modes reduce but do not eliminate the footprint; use a dedicated egress for sensitive targets.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Active scanning is detectable and may engage computer-misuse law

## 13. Alternatives

- [webappanalyzer](SUR-B2-07.md) ruleset applied in your own pipeline for a quieter approach
- [httpx](OSINT-C3-24.md) for fast HTTP probing across many hosts
- Passive sources (certificate transparency, DNS history) which leave no trace with the target

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/urbanadventurer/WhatWeb

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [mitmproxy](SUR-B2-06.md) | 96 | Adopt |
| 2 | [MobSF (Mobile Security Framework)](SUR-B2-04.md) | 88 | Adopt |
| 3 | [Citizen Lab publication directory](SUR-B2-20.md) | 86 | Reference only |
| 4 | [Exodus Privacy](SUR-B2-01.md) | 86 | Adopt |
| 5 | [USAspending.gov (custom award data)](SUR-B2-14.md) | 86 | Adopt |
| 6 | [Apktool](SUR-B2-05.md) | 86 | Adopt |
| 7 | [TED — Tenders Electronic Daily (EU public procurement)](SUR-B2-13.md) | 84 | Adopt |
| 8 | [DuckDuckGo Tracker Radar](SUR-B2-03.md) | 82 | Reference only |

---

← 297. [SSLyze](OSINT-C3-26.md) · 299. [OpenCellID](SUR-B2-19.md) →
