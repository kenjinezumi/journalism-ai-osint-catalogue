# SecureDrop Workstation

`SUR-B3-02` · **87/100** · overall rank 61 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 18) |
| **Segment** | B3 · Protecting journalists and sources (rank 13) |
| **Subcategory** | Secure submission |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Freedom of the Press Foundation |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/freedomofpress/securedrop-workstation) · [Documentation](https://workstation.securedrop.org/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 87/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Qubes OS-based journalist workstation for handling SecureDrop submissions, isolating networking, decryption, document viewing and export into separate virtual machines.

## Journalism / investigative use case

Replaces the air-gapped Secure Viewing Station with a single Qubes laptop where submissions are decrypted in one compartment, converted in another and read in a third — making the secure workflow something a journalist can plausibly follow daily rather than a procedure they avoid.

## 2. Audience

engineer, journalist

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Addresses the real failure mode of classic SecureDrop: the air-gapped workflow is onerous enough that journalists route around it, and compartmentalised-on-one-laptop is far more likely to be used as designed
- Qubes compartmentalisation means a malicious document that executes affects a disposable VM, not the journalist's machine — the same protection Dangerzone gives, applied structurally
- AGPL-3.0 and actively maintained (1.9.0, 2026-09-02; pushed 2026-11-16) by the same organisation as SecureDrop, so the pieces are designed together
- Documented, opinionated configuration reduces the chance of a newsroom improvising an insecure setup

## 5. Cons

- Requires Qubes OS on certified hardware, which is a narrow hardware compatibility list and a significant procurement constraint
- 268 open issues against only 189 stars — a high ratio indicating a complex system with a small user base, so you will encounter unresolved problems
- Qubes itself has a real learning curve; a journalist needs training and ongoing support, and the project does not remove that
- Still bound to a SecureDrop deployment, so it adds to rather than replaces the institutional commitment

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 189 stars with 268 open issues, release 1.9.0 (2026-09-02), pushed 2026-11-16, AGPL-3.0. FPF documents it as the recommended journalist-side workflow for SecureDrop, which is the relevant institutional signal.

## 7. Assessment

Adopt it alongside SecureDrop rather than as an alternative — the usability gain over the air-gapped SVS is the difference between a protocol that is followed and one that is nominally in place. For your profile the gating factor is hardware: confirm certified Qubes machines are procurable where you operate before committing, because in some exile contexts importing specific laptop models is itself difficult. Budget training time; Qubes is not intuitive.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release 1.9.0 (2026-09-02), 189 stars, 268 open issues. Current commits and versioned releases under institutional maintenance; the backlog reflects system complexity and a small contributor pool.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0; immaterial for internal deployment.

**Licence evidence:** https://github.com/freedomofpress/securedrop-workstation/blob/main/LICENSE

## 10. Costs

No software fee. Qubes-certified laptop per journalist handling submissions (estimate: upper four figures for a small team), plus training and support time. Replaces the SVS hardware cost rather than adding to it.

## 11. Privacy and data flows

Compartmentalised handling keeps decryption, viewing and export isolated, so a malicious submission cannot reach the journalist's general environment. Residual risk is the journalist's own operational discipline and the physical security of the laptop.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Requires Qubes-certified hardware; narrow compatibility list

## 13. Alternatives

- Classic air-gapped Secure Viewing Station if Qubes hardware is unobtainable
- [Dangerzone](SUR-B3-03.md) on an ordinary machine as a much weaker but far more available mitigation
- [Tails](SUR-B3-19.md) on a USB stick for ad-hoc isolated document handling

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/freedomofpress/securedrop-workstation
- https://workstation.securedrop.org/
- https://github.com/freedomofpress/securedrop-workstation/blob/main/LICENSE

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

← 60. [osm-search](OSINT-C2-27.md) · 62. [SimpleX Chat](SUR-B3-25.md) →
