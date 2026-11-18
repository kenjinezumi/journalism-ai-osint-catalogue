# Delta Chat / chatmail core

`SUR-B3-26` · **77/100** · overall rank 185 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 51) |
| **Segment** | B3 · Protecting journalists and sources (rank 27) |
| **Subcategory** | Secure communications |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Chatmail (transferred from deltachat/deltachat-core-rust) |
| **Maintenance** | Actively maintained |
| **Licence** | Not detected by the GitHub API — read the repository licence file (the Delta Chat/chatmail ecosystem is GPL-family) before redistribution |
| **Licence type** | Unresolved |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/chatmail/core) · [Documentation](https://delta.chat/en/help) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 3/5 · usability 4/5 · licence+cost 4/5 → **weighted 77/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Unresolved |
| **Exact licence (as recorded)** | Not detected by the GitHub API — read the repository licence file (the Delta Chat/chatmail ecosystem is GPL-family) before redistribution |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | Unverified in this survey; confirm from the repository before building a product on it. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** Free to use. Self-hosting a chatmail server: a small VM plus a mail domain — low cost and the configuration that makes the privacy properties real. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/chatmail/core
- https://delta.chat/en/help
- `../sources/evidence/leads.md`

> **Unresolved:** the licence could not be confirmed from the evidence gathered.

---

## 1. Purpose

Rust core library behind Delta Chat, providing end-to-end encrypted messaging over ordinary email infrastructure (SMTP/IMAP) with automatic Autocrypt-style key exchange, plus support for dedicated low-metadata 'chatmail' servers.

## Journalism / investigative use case

Encrypted messaging that travels over email, so it works wherever email works — including networks that block Signal and SimpleX. For a source in a country where messaging apps are blocked but email is not, Delta Chat may be the only encrypted channel available.

## 2. Audience

journalist, engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Using email as transport is the decisive property in censored networks: blocking Delta Chat means blocking email, which states are far more reluctant to do
- No new account needed in principle — a source with an email address can participate, lowering the adoption barrier that defeats other tools
- Chatmail servers are purpose-built to minimise retained metadata, and the ecosystem is self-hostable, so a newsroom can run its own
- Actively maintained (v2.69.0, 2026-11-09; pushed 2026-11-16) with the repository transfer deltachat/deltachat-core-rust → chatmail/core verified by redirect in this session

## 5. Cons

- Email metadata is the weak point: unless both parties use chatmail servers, the message path reveals sender, recipient and timing to mail providers — encryption protects content, not the relationship
- Using an existing email address links the conversation to an existing identity, which is the opposite of what anonymous first contact requires
- GitHub reports SPDX NOASSERTION, so the licence must be read from the repository (the project is GPL-family) before any redistribution
- 137 open issues and a complex interaction with diverse mail-server behaviour, so reliability varies by provider in ways that are hard to predict

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 950 stars with 137 open issues, release v2.69.0 (2026-11-09), pushed 2026-11-16, SPDX NOASSERTION; the repository transfer from deltachat/deltachat-core-rust to chatmail/core was confirmed by API redirect on 2026-11-17 and is recorded in leads.md L4. The chatmail server model is documented by the project.

## 7. Assessment

Keep it in the toolkit specifically as the censorship-resistant option — if Signal and SimpleX are blocked where your sources are, this is what remains. For your profile the configuration that matters is both parties on chatmail servers, which is what removes the mail-metadata problem; Delta Chat over ordinary mailboxes protects content while exposing the relationship, and that distinction must be explained to a source rather than assumed. Update any pinned references to the old deltachat-core-rust path.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v2.69.0 (2026-11-09), 950 stars, 137 open issues, SPDX NOASSERTION. Frequent releases under the renamed organisation; transfer verified by redirect.

## 9. Licensing

**Licence:** Not detected by the GitHub API — read the repository licence file (the Delta Chat/chatmail ecosystem is GPL-family) before redistribution _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Unverified in this survey; confirm from the repository before building a product on it.

**Licence evidence:** https://github.com/chatmail/core

## 10. Costs

Free to use. Self-hosting a chatmail server: a small VM plus a mail domain — low cost and the configuration that makes the privacy properties real. Estimate.

## 11. Privacy and data flows

Content is end-to-end encrypted. Metadata depends entirely on the servers: chatmail servers minimise retention, while ordinary mail providers see the sender-recipient relationship and timing. Choose the configuration deliberately and explain it to sources.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Mail metadata exposes the sender-recipient relationship unless both parties use chatmail servers

## 13. Alternatives

- Signal where it is reachable and a phone number is acceptable
- [SimpleX Chat](SUR-B3-25.md) for identifier-free contact where it is not blocked
- Tor plus any of the above where the network blocks everything

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/chatmail/core
- https://delta.chat/en/help
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

← 184. [Aleph (alephdata, original)](OSINT-C3-02.md) · 186. [FollowTheMoney (alephdata 3.x line)](JAI-A2-18.md) →
