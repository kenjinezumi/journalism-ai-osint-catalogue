# Hush Line

`SUR-B3-06` · **84/100** · overall rank 103 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 30) |
| **Segment** | B3 · Protecting journalists and sources (rank 18) |
| **Subcategory** | Secure submission |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Science & Design (scidsg) |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **Unknown / not verified** — not established by the records |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/scidsg/hushline) · [Documentation](https://hushline.app/) |

**Scores** — relevance 5/5 · capability 3/5 · maintenance 4/5 · privacy 4/5 · usability 5/5 · licence+cost 4/5 → **weighted 84/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | AGPL-3.0: a modified hosted instance obliges source publication. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **Unknown / not verified** — not established by the records |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure; staff effort |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Self-hosting: a small VM plus a Tor onion service — low. The hosted service has free and paid tiers whose current prices were NOT verified in this survey. Staff cost is PGP key management and monitoring the channel.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/scidsg/hushline/blob/main/LICENSE
- https://github.com/scidsg/hushline
- https://hushline.app/
- `../sources/evidence/leads.md`

> **Unresolved:** the price is not established by these records — this is not a statement that it is free.

---

## 1. Purpose

Lightweight anonymous tip-line service with end-to-end encryption to the recipient's PGP key, usable as a hosted service or self-hosted, with optional Tor onion access.

## Journalism / investigative use case

The realistic middle option between an email address and SecureDrop: a reporter publishes a Hush Line address, tips arrive encrypted to their key, and no infrastructure project is required. For a small outlet or an individual journalist, this is the difference between having a protected channel and having none.

## 2. Audience

journalist, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Fills the gap that matters most in practice — most journalists have no protected tip channel at all because SecureDrop is too heavy, and this is deployable by one person
- End-to-end encryption to the recipient's PGP key means the service operator cannot read tips, which is the key property for a hosted option
- AGPL-3.0, actively released (v0.7.36, 2026-11-05) with a small clean backlog (13 open issues), self-hostable if you prefer not to rely on the hosted service
- Tor onion access available, so a source with a serious threat model gets network-level protection too

## 5. Cons

- Smaller and younger than the alternatives (136 stars), so it has far less independent security scrutiny than SecureDrop — which matters for software in a source-protection path
- Hosted mode means the operator sees metadata (when tips arrive, to whom) even though content is encrypted, and that metadata can be revealing
- Depends on the journalist managing a PGP key correctly, which is historically where encrypted-tip workflows fail
- Session 1's candidate path (freedomofpress/hushline) is a 404 — the project is at scidsg/hushline, which is worth noting since the wrong path appears in older notes

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 136 stars with 13 open issues, release v0.7.36 (2026-11-05), pushed 2026-11-14, AGPL-3.0. The corrected repository path (scidsg/hushline, not freedomofpress/hushline) was established in this session's 404 sweep and is recorded in leads.md.

## 7. Assessment

Adopt it for individual reporters and small desks that will not run SecureDrop — a protected channel that exists beats a perfect one that does not. For your profile I would self-host rather than use the hosted service so the arrival metadata stays with you, and I would pair deployment with actual PGP key management support for the journalists involved, because that is the step that silently fails. Be honest in public about the protection level: it is not SecureDrop, and sources at state-level risk should be directed accordingly.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-14, latest release v0.7.36 (2026-11-05), 136 stars, 13 open issues. Frequent releases and a clean tracker from a small organisation; young project, so maintenance is assessed on cadence rather than track record.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0: a modified hosted instance obliges source publication.

**Licence evidence:** https://github.com/scidsg/hushline/blob/main/LICENSE

## 10. Costs

Self-hosting: a small VM plus a Tor onion service — low. The hosted service has free and paid tiers whose current prices were NOT verified in this survey. Staff cost is PGP key management and monitoring the channel.

## 11. Privacy and data flows

Content is end-to-end encrypted to the recipient's key, so even a hosted operator cannot read tips. Hosted mode still exposes arrival metadata to the operator; self-hosting removes that. Tor access protects source network identity where available.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [SecureDrop](SUR-B3-01.md) where the threat model justifies the operational commitment
- [OnionShare](SUR-B3-04.md) receive mode for a zero-infrastructure drop box
- A published Signal number, which is simpler but requires the source to reveal a phone number

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/scidsg/hushline
- https://hushline.app/
- `../sources/evidence/leads.md`

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

← 102. [csvkit](JAI-A1-18.md) · 104. [CourtListener](OSINT-C3-11.md) →
