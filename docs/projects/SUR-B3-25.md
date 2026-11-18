# SimpleX Chat

`SUR-B3-25` · **87/100** · overall rank 62 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 19) |
| **Segment** | B3 · Protecting journalists and sources (rank 14) |
| **Subcategory** | Secure communications |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | SimpleX Chat Ltd |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/simplex-chat/simplex-chat) · [Documentation](https://simplex.chat/docs/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 87/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | AGPL-3.0: a modified self-hosted relay offered to users obliges source publication. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Free to use. Self-hosting relays: a small VM each — low cost and worth it for metadata control. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/simplex-chat/simplex-chat/blob/stable/LICENSE
- https://github.com/simplex-chat/simplex-chat
- https://simplex.chat/docs/

---

## 1. Purpose

Messaging network with no user identifiers of any kind: contacts connect via one-time invitation links through relay servers that hold no account records, with end-to-end encryption and optional self-hosted relays.

## Journalism / investigative use case

First contact with a source who must not reveal a phone number, email address or any persistent identifier — the gap Signal cannot fill. A reporter publishes a one-time invitation link, the source connects, and no account exists on either side to be subpoenaed or correlated.

## 2. Audience

journalist, specialist investigator, engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- No user identifiers at all is a genuinely different architecture, not a privacy feature bolted on — there is no account, no phone number and no username to correlate or compel
- Self-hostable relays mean a newsroom can run its own infrastructure, so even relay metadata stays within your control
- AGPL-3.0 and very actively maintained (v7.1.4, 2026-11-14; pushed 2026-11-17) with a large community (19,711 stars)
- Fills the specific operational gap between anonymous submission systems and identified messaging, which nothing else here covers well

## 5. Cons

- 1,333 open issues — the largest backlog of any communications tool here — reflecting a young, fast-moving project; security-critical software with that profile warrants caution for the highest-risk use
- Far less independent cryptographic review than Signal, which is the decisive consideration when the threat is a state adversary — novel architecture means novel risk
- Usability is weaker than Signal: invitation-link exchange is unfamiliar, and because there are no accounts, losing the app or device can mean losing contacts irrecoverably
- A source must install an app nobody has heard of, which is itself a barrier and, in a hostile environment, a conspicuous artefact on their device

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 19,711 stars with 1,333 open issues, release v7.1.4 (2026-11-14), pushed 2026-11-17, AGPL-3.0. The identifier-free design is documented by the project; the volume of open issues relative to other messengers here is the notable signal and is visible in the API data.

## 7. Assessment

Pilot it for the identifier-free first-contact case, where it does something nothing else does — but do not displace Signal for ongoing source communication, because Signal's review record matters more than SimpleX's architectural elegance when the adversary is capable. For your profile the sensible posture is: publish a SimpleX invitation alongside your SecureDrop or Hush Line address as an alternative for sources who want live conversation without an identifier, self-host the relay, and keep Signal as the workhorse.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v7.1.4 (2026-11-14), 19,711 stars, 1,333 open issues. Same-day commits and a rapid release cadence; the large backlog indicates a project moving faster than it can close issues, which is a maturity caveat rather than a neglect signal.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0: a modified self-hosted relay offered to users obliges source publication.

**Licence evidence:** https://github.com/simplex-chat/simplex-chat/blob/stable/LICENSE

## 10. Costs

Free to use. Self-hosting relays: a small VM each — low cost and worth it for metadata control. Estimate.

## 11. Privacy and data flows

Architecturally the strongest metadata position of any messenger here: no identifiers, no accounts, and relays that hold no user records; self-hosting removes even relay-operator visibility. The counterweight is maturity — less reviewed code in a source-protection path is itself a risk.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Much less independent cryptographic review than Signal; large open-issue backlog for security-critical software

## 13. Alternatives

- Signal for a reviewed, ubiquitous channel where a phone number is acceptable
- [SecureDrop](SUR-B3-01.md) for anonymous document submission rather than conversation
- Briar for peer-to-peer messaging over Tor with no servers at all

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/simplex-chat/simplex-chat
- https://simplex.chat/docs/
- https://github.com/simplex-chat/simplex-chat/blob/stable/LICENSE

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

← 61. [SecureDrop Workstation](SUR-B3-02.md) · 63. [Apache Tika](JAI-A2-02.md) →
