# MVT (Mobile Verification Toolkit)

`SUR-B3-08` · **90/100** · overall rank 38 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 11) |
| **Segment** | B3 · Protecting journalists and sources (rank 9) |
| **Subcategory** | Device forensics |
| **Type** | cli |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | MVT Project (Amnesty International Security Lab lineage) |
| **Maintenance** | Actively maintained |
| **Licence** | MVT License 1.1 — NOT OSI-approved (MPL-2.0 derivative with a Consensual Use Restriction at §3.0); GitHub reports NOASSERTION |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/mvt-project/mvt) · [Documentation](https://docs.mvt.re/) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 5/5 · privacy 5/5 · usability 2/5 · licence+cost 3/5 → **weighted 90/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Forensic toolkit that acquires and analyses iOS backups and filesystem dumps and Android device data, checking them against indicators of compromise for mercenary spyware such as Pegasus and Predator.

## Journalism / investigative use case

The standard tool for answering 'has this journalist's phone been targeted?' — running a consensual check on a reporter's or source's device against published spyware indicators, which is how most publicly confirmed Pegasus infections of journalists have been established.

## 2. Audience

specialist investigator, engineer

## 3. Project type

cli · bucket `source-available-restricted`

## 4. Pros

- The reference implementation in this field, with direct lineage to the Amnesty Security Lab work that exposed Pegasus targeting of journalists — provenance no alternative matches
- Works against standard iOS backups, so a check can be run without jailbreaking or specialist hardware, which makes consensual checks practical in the field
- Very actively maintained (v2026.11.2, 2026-11-02; pushed 2026-11-17) with 16,096 stars and a modest backlog (66 open issues)
- Indicator-driven: pair it with Amnesty's published IOCs and stalkerware-indicators to extend coverage beyond mercenary spyware

## 5. Cons

- LICENCE BLOCKER, verified with primary evidence: MVT License 1.1 §3.0 imposes a Consensual Use Restriction requiring the Data Owner's explicit, uncoerced and fully informed consent, including disclosure of privacy implications and the data-retention policy. This is a contractual obligation, not merely ethics, and it is not an OSI licence
- A clean result is not evidence of safety: MVT finds known indicators, so a novel or well-cleaned implant is invisible, and reporting 'no infection found' as 'not targeted' would be wrong
- iOS coverage is substantially better than Android, where acquisition is harder and artefacts are fewer — so Android results are weaker and need androidqf plus more care
- Interpreting output requires forensic literacy; a false positive communicated badly to a journalist causes real distress, and a missed detection creates false confidence

## 6. Feedback (documented)

No individual user reports verified in this survey. The decisive documented fact is the licence, read in full from the repository: MVT License 1.1 §3.0 quoted verbatim in sources/evidence/leads.md with the full text saved at sources/recovered/cat/mvt.txt. 16,096 stars with 66 open issues; release v2026.11.2 (2026-11-02). MVT's role in confirmed Pegasus cases is publicly documented by Amnesty International.

## 7. Assessment

Adopt it, and build the licence obligation into your process rather than treating it as background: a written consent script that explains what is collected, what it reveals and how long you keep it, plus a retention policy you actually follow. That satisfies §3.0 and is good practice anyway. Two communication rules matter as much as the tooling: never describe a clean result as proof of safety, and never deliver a positive result to a journalist without a plan for what happens next — device replacement, account recovery, legal and psychological support.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v2026.11.2 (2026-11-02), 16,096 stars, 66 open issues. Same-day commits with date-versioned releases; institutional lineage and an active indicator-update cadence.

## 9. Licensing

**Licence:** MVT License 1.1 — NOT OSI-approved (MPL-2.0 derivative with a Consensual Use Restriction at §3.0); GitHub reports NOASSERTION _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Indicators of compromise come from Amnesty and other publishers under their own terms.

**Restrictions:** §3.0 Consensual Use Restriction (verbatim): use is permitted provided 'the Data Owner must explicitly consent to the procedure, free from any form of coercion, and must be fully informed about the nature of the procedure, its privacy implications, and any data retention and disposal policy.' Non-consensual forensic acquisition is prohibited. The restriction flows downstream on redistribution, and MPL-style file-level copyleft also applies.

**Licence evidence:** https://github.com/mvt-project/mvt/blob/main/LICENSE

## 10. Costs

No fee. A forensic workstation and storage for backups (phone backups are tens of GB each). The real cost is skilled analyst time per examination plus the consent and support process around it. Estimate.

## 11. Privacy and data flows

Processing is local, which is essential since a phone backup is the most intimate dataset a journalist will ever hand you. The obligations are correspondingly serious: encrypted storage, a short retention period, documented disposal, and access limited to the examining analyst. The licence makes several of these contractual rather than optional.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- MVT License 1.1 §3.0 consensual-use restriction — written informed consent and a disclosed retention policy are contractual requirements, and the licence is not OSI-approved

## 13. Alternatives

- [androidqf](SUR-B3-09.md) for Android acquisition before MVT analysis
- [iLEAPP](SUR-B3-15.md) and ALEAPP for broader artefact parsing beyond spyware indicators
- Referral to Amnesty Security Lab, Access Now's Digital Security Helpline or Citizen Lab where the stakes are high and in-house capacity is thin

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `repo-inspected`

- https://github.com/mvt-project/mvt/blob/main/LICENSE
- https://docs.mvt.re/
- `../sources/evidence/leads.md`
- `../sources/recovered/cat/mvt.txt`

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

← 37. [x-ray](JAI-A4-23.md) · 39. [Buzz](JAI-A2-05.md) →
