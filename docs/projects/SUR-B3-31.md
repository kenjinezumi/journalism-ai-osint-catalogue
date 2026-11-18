# Outline

`SUR-B3-31` · **86/100** · overall rank 70 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 23) |
| **Segment** | B3 · Protecting journalists and sources (rank 16) |
| **Subcategory** | Censorship circumvention |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Outline Foundation (transferred from Jigsaw-Code) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/OutlineFoundation/outline-apps) · [Documentation](https://getoutline.org/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 4/5 · licence+cost 4/5 → **weighted 86/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No software fee. Infrastructure: a VPS per server (low single-digit monthly cost each, estimate) plus bandwidth, and — the real cost — periodic replacement of blocked servers. Budget for several servers and rotation rather than one.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/OutlineFoundation/outline-apps/blob/master/LICENSE
- https://github.com/OutlineFoundation/outline-apps
- https://getoutline.org/
- `../sources/evidence/leads.md`

---

## 1. Purpose

VPN system built on Shadowsocks that lets an organisation run its own servers and distribute access keys, with a manager application for creating servers and clients for all major platforms.

## Journalism / investigative use case

Giving reporters and sources in censored countries a circumvention channel the newsroom controls: you run the server, distribute keys to specific people, and revoke them individually — rather than relying on a commercial VPN whose infrastructure, logging and blocking status are outside your control.

## 2. Audience

engineer, journalist

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- You control the infrastructure, which is the decisive difference from a commercial VPN: no third-party logs, no shared IP reputation, and keys you can revoke per person
- Shadowsocks-based transport is designed to resist protocol-based blocking, so it survives in networks where standard VPN protocols are detected and dropped
- Apache-2.0 with very active development (pushed 2026-11-17) and clients for all major platforms, so a mixed-device team is covered
- Repository transfer Jigsaw-Code/outline-apps → OutlineFoundation/outline-apps verified by redirect — governance moved from Google's Jigsaw to an independent foundation, which is arguably an improvement for this use case

## 5. Cons

- Release metadata is badly stale (v1.10.1 from 2023-03-20 against a windows-v1.9.1 tag) despite current commits, so determining what version users should run takes effort — a real problem for security software
- 595 open issues across a multi-platform client suite
- Running your own circumvention server makes you responsible for its operational security, and a server compromised by the adversary becomes a surveillance point on your most at-risk users
- Circumvention is an arms race: your server's IP can be blocked, and maintaining access means rotating infrastructure, which is ongoing work rather than a one-time deployment

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 9,282 stars with 595 open issues, release v1.10.1 (2023-03-20) against current commits (pushed 2026-11-17), Apache-2.0; transfer from Jigsaw-Code to OutlineFoundation confirmed by API redirect on 2026-11-17. Outline's design for organisational circumvention is documented by the project.

## 7. Assessment

Adopt it if you support people in censored networks — controlling your own circumvention infrastructure is materially better than recommending a commercial VPN. For your profile the realities to plan for: budget for IP rotation because servers get blocked, distribute keys through a channel that is itself protected, and treat the server as a high-value target since it sits in the path of your most exposed users' traffic. The stale release metadata is an irritant: pin and document the client versions you deploy.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release object v1.10.1 (2023-03-20), tag windows-v1.9.1, 9,282 stars, 595 open issues. Same-day commits with abandoned release tagging; activity is unambiguous but release hygiene is poor, which matters for a security tool.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material.

**Licence evidence:** https://github.com/OutlineFoundation/outline-apps/blob/master/LICENSE

## 10. Costs

No software fee. Infrastructure: a VPS per server (low single-digit monthly cost each, estimate) plus bandwidth, and — the real cost — periodic replacement of blocked servers. Budget for several servers and rotation rather than one.

## 11. Privacy and data flows

You hold the infrastructure, so there is no third-party logging. The counterpart responsibility is that your server sees users' traffic destinations, making its security and your logging policy a source-protection question in their own right. Set logging to minimal deliberately.

## 12. Verdict

**Adopt**

## 13. Alternatives

- Tor with bridges where anonymity rather than access is the goal
- Commercial VPNs for convenience, accepting third-party trust and shared blocking
- Self-hosted WireGuard where protocol-based blocking is not the problem

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/OutlineFoundation/outline-apps
- https://getoutline.org/
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

← 69. [GlobaLeaks](SUR-B3-05.md) · 71. [USAspending.gov (custom award data)](SUR-B2-14.md) →
