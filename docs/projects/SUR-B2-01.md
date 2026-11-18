# Exodus Privacy

`SUR-B2-01` · **86/100** · overall rank 68 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 21) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 4) |
| **Subcategory** | Tracker analysis (mobile) |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Exodus Privacy (association) |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Exodus-Privacy/exodus) · [Documentation](https://exodus-privacy.eu.org/en/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 4/5 · licence+cost 4/5 → **weighted 86/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | The tracker database is published by the project; check its terms before redistributing the database itself. |
| **Restrictions** | AGPL-3.0: a modified self-hosted instance offered to users obliges source publication. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Public instance free. Self-hosting estimate: a Django application plus static-analysis workers — one modest VM. Assumptions: occasional analysis volume.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/Exodus-Privacy/exodus/blob/v3/LICENSE
- https://github.com/Exodus-Privacy/exodus
- https://exodus-privacy.eu.org/en/
- `../sources/evidence/b2-sources.md`

---

## 1. Purpose

Platform that statically analyses Android applications to identify embedded trackers and requested permissions, publishing per-app reports and maintaining a public tracker database.

## Journalism / investigative use case

Establishing what an app actually does to its users: analyse a government service app, a state-promoted messaging app or a commercial app a story concerns, and show which tracking SDKs it embeds and what permissions it demands. For reporting on state apps that surveil citizens, this is the evidence base.

## 2. Audience

newsroom analyst, specialist investigator, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Produces citable per-app reports with a named tracker list, which converts a vague privacy concern into a specific, checkable finding a reader can verify
- The maintained tracker database is itself the asset: identifying an SDK as belonging to a particular data broker is the analytical step most reporters cannot do alone
- AGPL-3.0 and self-hostable, so you can analyse an app that the public instance has not covered or that you do not want to publicly request
- Actively maintained (v1.33.0, 2026-09-13; pushed the same day) by a focused association with 820 stars

## 5. Cons

- Static analysis identifies embedded SDKs, not actual behaviour: an app may include a tracker it never activates, or exfiltrate data through code the analysis does not flag — so a report is evidence of capability rather than of conduct
- Android only, so iOS apps (and therefore a large share of apps used in wealthier markets) are out of scope
- Requesting an analysis on the public instance is a public act, disclosing your interest in a specific app — self-host if that matters
- Tracker attribution depends on the database's completeness, so a novel or in-house tracking SDK will be missed or unnamed

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 820 stars with 52 open issues, release v1.33.0 (2026-09-13) with same-day push, AGPL-3.0. Exodus reports are widely cited in privacy journalism and advocacy, and the project publishes its methodology — note that session 1's URL for the tracker list (exodus-privacy.eu.org/en/page/trackers/) now 404s; the current entry point is the site root (verified 2026-11-17).

## 7. Assessment

Adopt it as the first step in any story about an app's data practices, and pair it with dynamic analysis (mitmproxy) before publishing a claim about what an app sends — static presence of an SDK and observed transmission are different claims, and the stronger story uses both. For your profile the self-hosting option matters: if the app you are examining belongs to a government you are investigating, a public analysis request is a tip-off.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-09-13, latest release v1.33.0 published the same day, 820 stars, 52 open issues. Regular releases from an established association that also operates the public analysis service.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** The tracker database is published by the project; check its terms before redistributing the database itself.

**Restrictions:** AGPL-3.0: a modified self-hosted instance offered to users obliges source publication.

**Licence evidence:** https://github.com/Exodus-Privacy/exodus/blob/v3/LICENSE

## 10. Costs

No fee. Public instance free. Self-hosting estimate: a Django application plus static-analysis workers — one modest VM. Assumptions: occasional analysis volume.

## 11. Privacy and data flows

Self-hosting keeps your analysis requests private. Using the public instance publishes the fact that an app was analysed, which discloses interest. The analysis itself involves no user data.

## 12. Verdict

**Adopt**

## 13. Alternatives

- MobSF for deeper static and dynamic app analysis you run yourself
- [mitmproxy](SUR-B2-06.md) to observe what an app actually transmits
- [Apktool](SUR-B2-05.md) for manual reverse engineering of a specific app

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/Exodus-Privacy/exodus
- https://exodus-privacy.eu.org/en/
- `../sources/evidence/b2-sources.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [mitmproxy](SUR-B2-06.md) | 96 | Adopt |
| 2 | [MobSF (Mobile Security Framework)](SUR-B2-04.md) | 88 | Adopt |
| 3 | [Citizen Lab publication directory](SUR-B2-20.md) | 86 | Reference only |
| 5 | [USAspending.gov (custom award data)](SUR-B2-14.md) | 86 | Adopt |
| 6 | [Apktool](SUR-B2-05.md) | 86 | Adopt |
| 7 | [TED — Tenders Electronic Daily (EU public procurement)](SUR-B2-13.md) | 84 | Adopt |
| 8 | [DuckDuckGo Tracker Radar](SUR-B2-03.md) | 82 | Reference only |
| 9 | [Blacklight collector](SUR-B2-02.md) | 81 | Adopt |

---

← 67. [Citizen Lab publication directory](SUR-B2-20.md) · 69. [GlobaLeaks](SUR-B3-05.md) →
