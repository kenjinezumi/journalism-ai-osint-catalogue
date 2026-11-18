# CryptPad

`SUR-B3-27` · **92/100** · overall rank 23 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 6) |
| **Segment** | B3 · Protecting journalists and sources (rank 4) |
| **Subcategory** | Encrypted collaboration |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | XWiki SAS / CryptPad team |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/cryptpad/cryptpad) · [Documentation](https://docs.cryptpad.org/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 92/100**

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
| **Restrictions** | AGPL-3.0: a modified instance offered to users obliges source publication. Running the released version for your newsroom carries no obligation. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No software fee. Infrastructure estimate: a single VM with modest resources serves a small newsroom; storage grows with document history. Operating effort is moderate — it is a web application with a cryptographic front end, so updates matter. The public CryptPad instance has free and paid tiers whose prices were not verified here.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/cryptpad/cryptpad/blob/main/LICENSE
- https://github.com/cryptpad/cryptpad
- https://docs.cryptpad.org/

---

## 1. Purpose

End-to-end encrypted collaborative office suite — documents, spreadsheets, kanban, forms, polls — where the server stores only ciphertext and encryption keys travel in the URL fragment.

## Journalism / investigative use case

Collaborative drafting and shared notes on a sensitive investigation where the hosting provider must not be able to read the material — replacing Google Docs for the planning document, the source list and the draft, which is where newsrooms most often leak their own investigations to a third party.

## 2. Audience

journalist, newsroom analyst, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Zero-knowledge server design means the operator — including you, if self-hosted — cannot read documents, which is a structural answer to the Google Docs problem rather than a policy promise
- Covers the formats a newsroom actually collaborates in (documents, sheets, kanban, forms), so it can genuinely replace a cloud suite for sensitive work rather than only for text
- AGPL-3.0 and self-hostable, very actively maintained (2026.10.1 released 2026-11-10; pushed 2026-11-16) with a substantial community (8,087 stars)
- Link-based access with no account requirement makes it usable by an external collaborator or source without onboarding

## 5. Cons

- Keys in the URL fragment means link handling IS key handling: a link pasted into Slack, email or a chat log hands over the document, and this is the dominant real-world failure mode
- 372 open issues and a complex browser-side cryptographic application, so the attack surface is the browser and any compromise there defeats the encryption
- Performance and feature depth are below commercial office suites, which creates pressure to revert to Google Docs for convenience — a social problem that will decide whether adoption sticks
- Self-hosting requires real operations care, and a misconfigured instance (or a compromised server serving modified JavaScript) can undermine the encryption model entirely

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 8,087 stars with 372 open issues, release 2026.10.1 (2026-11-10), pushed 2026-11-16, AGPL-3.0. CryptPad's zero-knowledge model is documented by the project and it operates a public instance; the key-in-URL design is inherent and openly documented.

## 7. Assessment

Adopt it for sensitive collaborative work and self-host it, with one rule drilled into the team: the link is the key, so links go only through a channel you would send the document itself through. For your profile this replaces the single most common and least-discussed leak in investigative work — the shared planning document on a third-party cloud. Expect to actively defend adoption against the convenience of commercial suites; that is the real implementation challenge, not the deployment.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release 2026.10.1 (2026-11-10), 8,087 stars, 372 open issues. Frequent dated releases under a commercial sponsor (XWiki SAS) with public-instance operation.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0: a modified instance offered to users obliges source publication. Running the released version for your newsroom carries no obligation.

**Licence evidence:** https://github.com/cryptpad/cryptpad/blob/main/LICENSE

## 10. Costs

No software fee. Infrastructure estimate: a single VM with modest resources serves a small newsroom; storage grows with document history. Operating effort is moderate — it is a web application with a cryptographic front end, so updates matter. The public CryptPad instance has free and paid tiers whose prices were not verified here.

## 11. Privacy and data flows

The server stores only ciphertext, so a hosting compromise or legal demand yields nothing readable — the strongest property available for collaborative documents. The two residual risks are link disclosure (keys in URLs) and browser compromise, both of which are user-side and must be addressed by practice rather than configuration.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Document keys travel in URLs — link handling is key handling

## 13. Alternatives

- [Nextcloud](SUR-B3-28.md) with server-side or end-to-end encryption for a broader self-hosted suite with weaker confidentiality
- Etherpad self-hosted for simple shared text without encryption
- Local files plus encrypted transfer for the most sensitive documents, accepting the collaboration cost

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/cryptpad/cryptpad
- https://docs.cryptpad.org/
- https://github.com/cryptpad/cryptpad/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Signal (Android client)](SUR-B3-23.md) | 95 | Adopt |
| 2 | [mat2](SUR-B3-07.md) | 94 | Adopt |
| 3 | [SecureDrop](SUR-B3-01.md) | 92 | Adopt |
| 5 | [Dangerzone](SUR-B3-03.md) | 92 | Adopt |
| 6 | [OnionShare](SUR-B3-04.md) | 92 | Adopt |
| 7 | [Orbot](SUR-B3-30.md) | 92 | Adopt |
| 8 | [Tails](SUR-B3-19.md) | 92 | Adopt |
| 9 | [MVT (Mobile Verification Toolkit)](SUR-B3-08.md) | 90 | Adopt |

---

← 22. [SecureDrop](SUR-B3-01.md) · 24. [Dangerzone](SUR-B3-03.md) →
