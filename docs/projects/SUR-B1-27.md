# DataIndex.us (Federal Data Terminations Tracker)

`SUR-B1-27` · **62/100** · overall rank 310 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 74) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 23) |
| **Subcategory** | Public-dataset monitoring |
| **Type** | platform |
| **Bucket** | `proprietary-service` |
| **Maintainer** | Federation of American Scientists (FAS) |
| **Maintenance** | Uncertain |
| **Licence** | Not verified — the site states its code is GPL v3 but no public repository was found; terms of use for the data were not verified |
| **Licence type** | Proprietary |
| **Open-source status** | Proprietary |
| **Software price** | **No software fee** |
| **Confidence** | low · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Documentation](https://dataindex.us/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 2/5 · privacy 4/5 · usability 5/5 · licence+cost 2/5 → **weighted 62/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Proprietary |
| **Exact licence (as recorded)** | Not verified — the site states its code is GPL v3 but no public repository was found; terms of use for the data were not verified |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Not verified. Underlying federal sources are generally US government works (public domain in the US), but FAS's compilation and annotations may carry their own rights. |
| **Restrictions** | Unverified. Link and cite rather than republishing the compilation as a dataset. |
| **Open-source status** | **Proprietary** — Hosted service or proprietary software — governed by service terms, not a software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **low** |

**Recorded cost detail.** Free to read; newsletter free. No infrastructure. Not self-hostable in practice.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://dataindex.us/

---

## 1. Purpose

Hosted tracker documenting US federal datasets that have been terminated, altered or had variables removed, plus pending changes to statistical collections, with an email newsletter.

## Journalism / investigative use case

Check whether a federal dataset you are about to rely on has been terminated, altered or had variables removed — and pick up story leads from documented removals and pending collection changes. For reporting that depends on official statistics, this is a direct check on whether the ground has moved under a story.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

platform · bucket `proprietary-service`

## 4. Pros

- Addresses a real and under-covered problem: datasets disappear or change definition quietly, and a story built on last year's variable can be silently wrong
- Curated by a credible policy organisation with subject expertise, so entries carry context rather than just diffs
- Zero effort to use — a reporter reads the site or subscribes to the newsletter
- Documented removals are themselves story leads, not just defensive checks

## 5. Cons

- Despite the site's statement that its code is GPL v3, no public repository was found in this survey, so it cannot be verified as open-source software or self-hosted — treat it as a hosted dataset and dashboard
- Scope is US federal data only, so it does not help for other jurisdictions
- As a hosted third-party service it carries continuity risk: if it stops, the historical record of what was removed may not be preserved elsewhere
- Licence and terms unverified, so you should link to it rather than republish its contents as a dataset

## 6. Feedback (documented)

No individual user reports verified. Documented: no public repository was found during this survey despite the site's GPL v3 code statement — verified by search on 2026-11-17 and recorded as unresolved. The service is live with a newsletter.

## 7. Assessment

Worth adding to your routine as a pre-flight check whenever a story leans on US federal statistics, and worth subscribing to for leads. But treat it as a secondary source: when a removal matters to a story, corroborate against the agency's own site, the Federal Register notice, and an archived capture (Wayback or your own), and cite those. Also note the dependency asymmetry — a tracker of disappearing data that itself disappears is a known failure mode, so capture pages you rely on.

## 8. Maintenance

**Uncertain** — No public repository found in this survey, so repository-based assessment is impossible. The hosted site and newsletter were live as of this survey. Classified Uncertain because a hosted service's maintenance cannot be evidenced the way a repository's can, and the claimed open-source code could not be located.

## 9. Licensing

**Licence:** Not verified — the site states its code is GPL v3 but no public repository was found; terms of use for the data were not verified _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Not verified. Underlying federal sources are generally US government works (public domain in the US), but FAS's compilation and annotations may carry their own rights.

**Restrictions:** Unverified. Link and cite rather than republishing the compilation as a dataset.

**Licence evidence:** https://dataindex.us/

## 10. Costs

Free to read; newsletter free. No infrastructure. Not self-hostable in practice.

## 11. Privacy and data flows

Journalists read from the hosted site or email newsletter; no local data holding and no measurement. Subscribing discloses your interest and email address to FAS.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- No public repository located; licence and terms unverified; hosted single point of failure

## 13. Alternatives

- [EDGI web-monitoring-db](SUR-B1-20.md) for systematic self-hosted monitoring of agency pages and datasets
- Your own changedetection.io or webchanges watches on the specific dataset landing pages you depend on
- Internet Archive captures plus the wayback client for reconstructing what a dataset page said

## 14. Evidence

Verified **2026-11-17** · confidence **low** · assessment depth `docs-reviewed`

_Marked provisional: the evidence does not support a firm score._

- https://dataindex.us/

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

← 309. [ArchiveBot](OSINT-C1-26.md) · 311. [Internet Society Pulse](SUR-B1-14.md) →
