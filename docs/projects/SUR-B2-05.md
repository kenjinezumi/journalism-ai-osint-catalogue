# Apktool

`SUR-B2-05` · **86/100** · overall rank 74 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 25) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 6) |
| **Subcategory** | Mobile app reverse engineering |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Connor Tumbleson (iBotPeaches) and contributors |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/iBotPeaches/Apktool) · [Documentation](https://apktool.org/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 86/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Tool for reverse engineering Android APK files: decodes resources to near-original form, disassembles bytecode to smali, and can rebuild a modified APK.

## Journalism / investigative use case

Reading what an app actually contains: extract the hardcoded endpoints, API keys, strings and configuration from a surveillance or state app to show which servers it talks to and which third parties it embeds — often the most quotable evidence in an app investigation, because strings in a binary are hard to deny.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Resource and string extraction gives concrete, quotable artefacts (endpoint URLs, provider names, hidden configuration) that make an app story specific
- The foundational tool in this space — MobSF and most analysis pipelines depend on it — so understanding it underpins everything else
- Apache-2.0 with excellent maintenance: release v3.0.3 (2026-07-20), pushed 2026-11-16, 78 open issues against 27,258 stars
- Mature and stable, so results are reproducible across versions — important when an analysis will be challenged

## 5. Cons

- Produces smali rather than readable source, so understanding logic (as opposed to extracting strings) requires real reverse-engineering skill
- Obfuscated and packed apps resist analysis, and commercial spyware is typically heavily obfuscated — which is exactly the case you most want to analyse
- Reverse engineering may breach terms of service and local law; the rebuild capability in particular can stray into territory you do not want to be in during an investigation
- Narrow scope by design: it decodes, and everything analytical is yours to do

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 27,258 stars with 78 open issues, release v3.0.3 (2026-07-20), pushed 2026-11-16, Apache-2.0. Its position as the standard APK decoder is evidenced by MobSF and the wider Android-analysis ecosystem depending on it.

## 7. Assessment

Adopt as the low-level complement to MobSF — when you need to pull specific strings or configuration out of an APK, this is the tool, and the output is often the most publishable evidence in the story. For your profile the realistic expectation is that it works well on ordinary apps and poorly on deliberately obfuscated spyware; for the latter, the realistic route is a specialist partner (Amnesty Security Lab, Citizen Lab) rather than in-house analysis.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v3.0.3 (2026-07-20), 27,258 stars, 78 open issues. Long-running project with a consistent release history and a low backlog relative to scale.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material for the tool. The legal constraints are external: reverse-engineering prohibitions in app terms and, in some jurisdictions, in law.

**Licence evidence:** https://github.com/iBotPeaches/Apktool/blob/master/LICENSE.md

## 10. Costs

No fee. Java runtime; negligible resources.

## 11. Privacy and data flows

Entirely local decoding; the APK and your interest in it stay on your machine.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Reverse engineering may breach app terms and local law

## 13. Alternatives

- MobSF for an automated analysis pipeline built on this
- jadx for decompilation to more readable Java-like source
- A specialist forensic partner for obfuscated commercial spyware

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/iBotPeaches/Apktool
- https://apktool.org/
- https://github.com/iBotPeaches/Apktool/blob/master/LICENSE.md

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [mitmproxy](SUR-B2-06.md) | 96 | Adopt |
| 2 | [MobSF (Mobile Security Framework)](SUR-B2-04.md) | 88 | Adopt |
| 3 | [Citizen Lab publication directory](SUR-B2-20.md) | 86 | Reference only |
| 4 | [Exodus Privacy](SUR-B2-01.md) | 86 | Adopt |
| 5 | [USAspending.gov (custom award data)](SUR-B2-14.md) | 86 | Adopt |
| 7 | [TED — Tenders Electronic Daily (EU public procurement)](SUR-B2-13.md) | 84 | Adopt |
| 8 | [DuckDuckGo Tracker Radar](SUR-B2-03.md) | 82 | Reference only |
| 9 | [Blacklight collector](SUR-B2-02.md) | 81 | Adopt |

---

← 73. [PyMuPDF](JAI-A2-42.md) · 75. [rasterio](OSINT-C2-22.md) →
