# OONI Probe Multiplatform

`SUR-B1-02` · **85/100** · overall rank 84 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 28) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 5) |
| **Subcategory** | Censorship measurement |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Open Observatory of Network Interference (OONI) |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Licence type** | Mixed (code vs weights/data) |
| **Open-source status** | Mixed |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ooni/probe-multiplatform) · [Documentation](https://ooni.org/install/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 2/5 · usability 5/5 · licence+cost 4/5 → **weighted 85/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Mixed (code vs weights/data) |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Measurement data published as OONI open data; Citizen Lab test lists are CC-BY-NC-SA-4.0. |
| **Restrictions** | GPL-3.0; app-store distribution of GPL software has known friction on iOS — relevant only if you fork and redistribute. |
| **Open-source status** | **Mixed** — Open-source code, restricted data licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Free. No infrastructure. Cost is volunteer coordination and the duty-of-care briefing time.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/ooni/probe-multiplatform/blob/main/LICENSE
- https://github.com/ooni/probe-multiplatform
- https://ooni.org/install/

---

## 1. Purpose

Kotlin Multiplatform app for Android, iOS and desktop that runs the OONI test suite with a graphical interface and publishes results to OONI's collector.

## Journalism / investigative use case

Newsrooms can ask sources, correspondents or volunteer networks inside a country to install one app and run a standard test suite, producing comparable public measurements without any command-line skills — the practical route to building coverage of whether your own outlet is blocked across several ISPs.

## 2. Audience

journalist, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Removes the technical barrier entirely, which is what makes distributed measurement by non-technical volunteers possible at all
- Standardised test suite means results from different volunteers are directly comparable and aggregate into a usable dataset
- Very active (v6.3.1, 2026-11-09; pushed 2026-11-17) and consolidating previously separate Android/iOS codebases into one maintained project
- App-store distribution means volunteers do not need to trust a sideloaded binary

## 5. Cons

- Still an app the user must deliberately install and run, so coverage is opportunistic and biased toward activist and technical populations — the networks used by ordinary readers are under-sampled
- Installing and running a censorship-measurement app is itself a risk signal on a user's device in a repressive country, and the app's presence may be visible to someone inspecting the phone
- The older Android codebase is archived, so bug reports and older documentation point at dead code
- Results publish ASN, network name and country, so a volunteer on a small or identifiable network is not anonymous

## 6. Feedback (documented)

No individual user reports verified. Documented: the consolidation of previously separate platform codebases into probe-multiplatform (the older Android repository being archived), and the app's own disclosure that results are published as open data with network metadata. 99 stars, 32 open issues, release 2026-11-09.

## 7. Assessment

The right tool for commissioning distributed measurement, with a serious duty of care attached. For your profile I would (1) brief volunteers explicitly that the app is visible on their device and that their network is published, (2) prefer volunteers outside high-risk categories where possible, and (3) treat coverage gaps as evidence of nothing rather than evidence of no blocking. Used carefully it is how a small outlet can demonstrate that it is being blocked across multiple ISPs.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v6.3.1 (2026-11-09), 99 stars, 32 open issues. Current releases on a 6.x line; the deliberate consolidation of platform codebases is evidence of active engineering investment.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** Measurement data published as OONI open data; Citizen Lab test lists are CC-BY-NC-SA-4.0.

**Restrictions:** GPL-3.0; app-store distribution of GPL software has known friction on iOS — relevant only if you fork and redistribute.

**Licence evidence:** https://github.com/ooni/probe-multiplatform/blob/main/LICENSE

## 10. Costs

Free. No infrastructure. Cost is volunteer coordination and the duty-of-care briefing time.

## 11. Privacy and data flows

Results upload to OONI's collector and are republished as open data with ASN, network name and country. The app surfaces this, but a volunteer may not grasp the implication — explaining it is your responsibility. The app's presence on a device is itself a disclosure in a hostile-search scenario.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Volunteer risk: app presence on device plus published network metadata

## 13. Alternatives

- [OONI Explorer](SUR-B1-03.md) to use existing measurements without asking anyone to take risk
- OONI Probe CLI for technically capable operators needing scripted repetition
- IODA for country-level outage evidence with no in-country participation

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ooni/probe-multiplatform
- https://ooni.org/install/
- https://github.com/ooni/probe-multiplatform/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [changedetection.io](SUR-B1-15.md) | 93 | Adopt |
| 2 | [OONI Explorer](SUR-B1-03.md) | 90 | Adopt |
| 3 | [IODA (Internet Outage Detection and Analysis)](SUR-B1-07.md) | 88 | Adopt |
| 4 | [OONI Probe CLI / probe-engine](SUR-B1-01.md) | 85 | Adopt |
| 6 | [shot-scraper](SUR-B1-23.md) | 83 | Adopt |
| 7 | [webchanges](SUR-B1-17.md) | 82 | Adopt |
| 8 | [EDGI web-monitoring-diff](SUR-B1-21.md) | 81 | Integrate |
| 9 | [urlwatch](SUR-B1-16.md) | 80 | Integrate |

---

← 83. [androidqf](SUR-B3-09.md) · 85. [LibreTranslate](JAI-A2-27.md) →
