# Blacklight collector

`SUR-B2-02` · **81/100** · overall rank 135 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 37) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 9) |
| **Subcategory** | Tracker analysis (web) |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | The Markup |
| **Maintenance** | Stable with low activity |
| **Licence** | GPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/the-markup/blacklight-collector) · [Documentation](https://themarkup.org/blacklight) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 3/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 81/100**

---

## 1. Purpose

Node library that loads a web page in an instrumented browser and records its tracking behaviour: third-party cookies, canvas fingerprinting, session recording, key logging, Facebook pixel and Google Analytics presence, and data flows to third parties.

## Journalism / investigative use case

The engine behind The Markup's Blacklight investigations: scan a set of websites — government services, hospitals, benefits portals, a political campaign — and report which of them send visitor data to advertising and analytics companies. It turns 'this site has trackers' into an enumerated, reproducible finding across hundreds of sites.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Built by a newsroom for published investigations, so the measurements it takes are the ones that stand up editorially — session recording and key logging in particular are specific, explicable harms rather than abstract tracking
- Dynamic measurement of actual behaviour, which is stronger evidence than static SDK detection: it records what the page really did when loaded
- Scales to a survey: run it over hundreds of sites and you have a dataset, which is how the strongest tracker stories are built
- GPL-3.0 and actively maintained (release 3.11.0, 2026-06-04; pushed 2026-09-03) with the methodology published alongside The Markup's investigations

## 5. Cons

- Measures a single page load from your vantage point, so results vary with geography, consent banners and A/B variation — a survey needs a documented, repeated methodology rather than one run
- Your scanning traffic is visible to the target sites and to the tracking companies, so a large survey is detectable and your IP range may be flagged
- Last push 2026-09-03 with the release in June: maintenance is steady but not brisk, and 245 stars means a small community for a tool this useful
- Node/Puppeteer dependency surface and browser-version sensitivity, so reproducing a survey months later needs the environment pinned

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 245 stars with release @themarkup/blacklight-collector@3.11.0 (2026-06-04), pushed 2026-09-03, GPL-3.0. The Markup's published Blacklight investigations document the methodology and are the strongest evidence that the tool produces publishable findings. Session 1's candidate path mozilla/blacklight is a 404; the correct repository is the-markup/blacklight-collector (verified 2026-11-17).

## 7. Assessment

Adopt it for any story about who is watching visitors to a set of websites — it is one of the clearest cases in this catalogue of a tool built for and proven by published journalism. For your profile the methodological work matters more than the running: define the site list, the vantage point, the consent-handling behaviour and the repetition schedule in advance, and publish them, because the finding's credibility rests on reproducibility. Pin the environment so you can re-run it a year later.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-09-03, latest release @themarkup/blacklight-collector@3.11.0 (2026-06-04), 245 stars, GPL-3.0. Two months since last push and five since release; steady newsroom-maintained tooling rather than a fast-moving project.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a. Tracker-identification lists it relies on may have their own sources.

**Restrictions:** GPL-3.0: embedding in a distributed product triggers copyleft. Internal survey use is unaffected.

**Licence evidence:** https://github.com/the-markup/blacklight-collector/blob/main/LICENSE

## 10. Costs

No fee. Compute for browser-based scanning — a survey of a few hundred sites is hours on one machine. Negligible infrastructure. Estimate.

## 11. Privacy and data flows

Your scanning is visible to the target sites and to the trackers it triggers; it collects no personal data of your own. For a sensitive survey, scan from an egress not attributable to your newsroom.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Exodus Privacy](SUR-B2-01.md) for the mobile-app equivalent
- [DuckDuckGo Tracker Radar](SUR-B2-03.md) as a reference dataset on tracker ownership and behaviour
- OpenWPM for an academic-grade web-measurement platform

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/the-markup/blacklight-collector
- https://themarkup.org/blacklight
- `../sources/evidence/leads.md`

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

← 134. [Qdrant](JAI-A3-07.md) · 136. [c2pa-rs / c2patool](OSINT-C2-13.md) →
