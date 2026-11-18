# Qubes OS

`SUR-B3-20` · **89/100** · overall rank 45 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 14) |
| **Segment** | B3 · Protecting journalists and sources (rank 11) |
| **Subcategory** | Compartmentalised operating system |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Qubes OS Project |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-2.0 (project licensing; the distribution aggregates components under their own licences) |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/QubesOS/qubes-issues) · [Documentation](https://www.qubes-os.org/doc/) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 4/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 89/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-2.0 (project licensing; the distribution aggregates components under their own licences) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | Aggregate free-software licensing; immaterial for use. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Dedicated hardware; self-hosted infrastructure; staff effort |
| **Cost conditions** | Dedicated hardware; Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No software fee. Certified hardware is the cost: a Qubes-capable laptop with substantial RAM and SSD (estimate: mid-to-upper four figures for a small team), plus training and support time. The hardware constraint is the real budget item.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://www.qubes-os.org/doc/license/
- https://www.qubes-os.org/doc/
- https://github.com/QubesOS/qubes-issues

---

## 1. Purpose

Security-focused desktop operating system that runs applications in isolated Xen-based virtual machines organised by trust level, with disposable VMs, a separate networking VM and controlled inter-VM file transfer.

## Journalism / investigative use case

A daily-use environment where compromise is contained: open an untrusted attachment in a disposable VM that is destroyed afterwards, keep source communications in one compartment and ordinary browsing in another, so a malicious document or a phishing click cannot reach your notes or your keys.

## 2. Audience

engineer, specialist investigator, journalist

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Compartmentalisation is the only architecture here that assumes compromise will happen and limits what it reaches — the right model for a journalist who must open attachments from strangers
- Disposable VMs make opening an untrusted document safe by construction, which is Dangerzone's protection generalised to everything
- Underpins SecureDrop Workstation, so adopting Qubes brings the recommended submission-handling workflow within reach
- Long-standing project with institutional respect in the security community and a documented release and security-advisory process

## 5. Cons

- Hardware compatibility is genuinely restrictive: Qubes needs specific virtualisation and IOMMU support, and the certified-hardware list is short — procurement is the first obstacle and in some regions a decisive one
- Steep learning curve and real daily friction: moving files between compartments is deliberate work, and users who find it tedious will subvert it
- The GitHub presence is an issue tracker (QubesOS/qubes-issues, no releases, no detected licence), so repository metadata tells you nothing about the OS's health — assessment must come from the project's own release and advisory channels
- Resource-hungry: comfortable use needs substantial RAM and a fast SSD, so older laptops are unusable

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the GitHub repository QubesOS/qubes-issues is a tracker (624 stars, no releases, last push 2026-07-08, no detected licence) rather than the OS source, so maintenance was not assessed from it. Qubes's adoption in high-threat journalism and its use as the basis of SecureDrop Workstation are documented by FPF.

## 7. Assessment

Adopt for the people who most need it — reporters handling unsolicited material and anyone working on a high-risk investigation — provided you can procure certified hardware and support the learning curve. For your profile the realistic path is a small number of Qubes machines for specific roles rather than an organisation-wide rollout, paired with SecureDrop Workstation if you run a submission system. Where Qubes is impractical, Tails for sessions plus Dangerzone for documents covers much of the same risk at far lower cost.

## 8. Maintenance

**Actively maintained** — Assessed from the project's own release and security-advisory process rather than GitHub, since QubesOS/qubes-issues is only a tracker (no releases, pushed 2026-07-08, no detected licence). The project maintains a published advisory stream and a certified-hardware programme; this classification is therefore medium-confidence on evidence type, not on the conclusion.

## 9. Licensing

**Licence:** GPL-2.0 (project licensing; the distribution aggregates components under their own licences) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Aggregate free-software licensing; immaterial for use.

**Licence evidence:** https://www.qubes-os.org/doc/license/

## 10. Costs

No software fee. Certified hardware is the cost: a Qubes-capable laptop with substantial RAM and SSD (estimate: mid-to-upper four figures for a small team), plus training and support time. The hardware constraint is the real budget item.

## 11. Privacy and data flows

Compartmentalisation limits what a compromise reaches, and the networking VM isolates the network stack. It is not an anonymity system — Qubes protects against compromise, Tails protects against tracing, and they answer different questions. Whonix VMs inside Qubes combine both.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Restrictive certified-hardware requirement; substantial learning curve and resource needs

## 13. Alternatives

- [Tails](SUR-B3-19.md) for amnesic, Tor-routed sessions rather than daily compartmentalisation
- [Dangerzone](SUR-B3-03.md) plus a hardened conventional OS as a much cheaper partial mitigation
- A dedicated, network-isolated laptop for the highest-risk material

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `docs-reviewed`

- https://www.qubes-os.org/doc/
- https://github.com/QubesOS/qubes-issues

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

← 44. [spaCy](JAI-A2-47.md) · 46. [RSSHub](JAI-A1-05.md) →
