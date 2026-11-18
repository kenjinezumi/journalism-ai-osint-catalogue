# Citizen Lab URL test lists

`SUR-B1-06` · **75/100** · overall rank 207 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 58) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 17) |
| **Subcategory** | Censorship measurement input data |
| **Type** | dataset |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | Citizen Lab (University of Toronto) |
| **Maintenance** | Actively maintained |
| **Licence** | CC-BY-NC-SA-4.0 (asserted in project documentation; no LICENSE file in the repository root and GitHub reports no SPDX) |
| **Licence type** | Restricted / non-OSI |
| **Open-source status** | Source available |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/citizenlab/test-lists) · [Documentation](https://github.com/citizenlab/test-lists#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 2/5 → **weighted 75/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Restricted / non-OSI |
| **Exact licence (as recorded)** | CC-BY-NC-SA-4.0 (asserted in project documentation; no LICENSE file in the repository root and GitHub reports no SPDX) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Same — this is a dataset, not software. |
| **Restrictions** | NonCommercial bars commercial redistribution or productisation; ShareAlike requires derived lists to carry the same licence. A commercially operated newsroom cannot assume its use is non-commercial. Reading and testing against the lists is ordinary use; republishing them is not. |
| **Open-source status** | **Source available** — Restricted data licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. No infrastructure. Cost is the effort of submitting additions and tracking whether they are merged.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/citizenlab/test-lists

---

## 1. Purpose

Curated per-country and global lists of URLs categorised by topic (news media, human rights, political criticism, LGBT, circumvention tools) that drive censorship-measurement testing.

## Journalism / investigative use case

Defines what gets tested, so a newsroom can check whether the outlets it cares about are even in the list for a country — and submit them if not — before citing OONI coverage as evidence of press blocking. If your outlet is not on the list, nobody has been testing whether you are blocked.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

dataset · bucket `source-available-restricted`

## 4. Pros

- Directly actionable: adding your own domains via pull request means future OONI measurements will test them, turning a coverage gap into evidence over time
- Topic categorisation lets you make statements about classes of censorship (news media versus circumvention tools) rather than single sites
- Maintained with real community input (pushed 2026-11-04, 554 stars, active PR flow)
- Static data in git, so it is trivially auditable and versioned — you can show what the list contained on a given date

## 5. Cons

- CC-BY-NC-SA-4.0: the NonCommercial clause is a genuine problem for commercial newsrooms wanting to redistribute the lists or build products on them, and ShareAlike propagates to derived lists — legal review is warranted
- There is no LICENSE file in the repository root (GitHub reports no SPDX), so the licence is asserted in documentation rather than detected — an extra verification step for your compliance records
- 148 open issues, many of them pending list submissions, so inclusion is not immediate
- List composition reflects curatorial judgement, and under-coverage of a country's independent media is a real and consequential gap

## 6. Feedback (documented)

No individual user reports verified. Documented: the CC-BY-NC-SA-4.0 licence and the absence of a root LICENSE file (verified session 1, retained); 148 open issues including submission backlog; 554 stars.

## 7. Assessment

Do two things with this: check whether your own and partner outlets' domains are listed for the countries you care about, and submit them if not — that is a concrete, cheap action that improves the evidence base for your own future reporting. Then handle the licence carefully: reading and acting on the list is fine, redistributing it or building a commercial product on it is not, and 'we are a newsroom' does not satisfy NonCommercial.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-04, no releases (git-tracked data), SPDX none, 554 stars, 148 open issues. Continuous community contributions with institutional curation by Citizen Lab; the open-issue count is largely submission queue rather than defects.

## 9. Licensing

**Licence:** CC-BY-NC-SA-4.0 (asserted in project documentation; no LICENSE file in the repository root and GitHub reports no SPDX) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same — this is a dataset, not software.

**Restrictions:** NonCommercial bars commercial redistribution or productisation; ShareAlike requires derived lists to carry the same licence. A commercially operated newsroom cannot assume its use is non-commercial. Reading and testing against the lists is ordinary use; republishing them is not.

**Licence evidence:** https://github.com/citizenlab/test-lists

## 10. Costs

No fee. No infrastructure. Cost is the effort of submitting additions and tracking whether they are merged.

## 11. Privacy and data flows

Static public data in git; no measurement or personal data involved. Note that submitting your outlet's domains is a public act that signals interest in its censorship status.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- CC-BY-NC-SA-4.0 NonCommercial clause — blocks commercial redistribution and productisation

## 13. Alternatives

- OONI's own category definitions for understanding what coverage means
- Maintaining a private internal list for your own direct testing, avoiding the NC licence entirely
- Commissioning targeted measurement of specific domains via OONI Probe

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `repo-inspected`

- https://github.com/citizenlab/test-lists

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

← 206. [Ushahidi Platform](OSINT-C3-07.md) · 208. [dnstwist](OSINT-C3-25.md) →
