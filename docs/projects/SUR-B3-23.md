# Signal (Android client)

`SUR-B3-23` · **95/100** · overall rank 5 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 2) |
| **Segment** | B3 · Protecting journalists and sources (rank 1) |
| **Subcategory** | Secure communications |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Signal Foundation |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/signalapp/Signal-Android) · [Documentation](https://support.signal.org/) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 5/5 · privacy 4/5 · usability 5/5 · licence+cost 4/5 → **weighted 95/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

End-to-end encrypted messaging application for text, voice and video, with disappearing messages, sealed sender, safety numbers for key verification and encrypted group messaging.

## Journalism / investigative use case

The default channel for source communication where a phone number is acceptable: messages and calls are end-to-end encrypted, disappearing messages limit what a seized device reveals, and the protocol is the most scrutinised in the field. In practice it is the channel most sources already have.

## 2. Audience

journalist, newsroom analyst, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- The most heavily analysed end-to-end encryption protocol in general use, with repeated independent cryptographic review — the strongest assurance basis of any communications tool here
- Disappearing messages and remote-deletion materially reduce what a seized or compromised device yields, which is the realistic threat for most journalists
- AGPL-3.0 client and server, actively maintained (v8.35.2, 2026-11-09; pushed 2026-11-16), with reproducible-build efforts and a non-profit operator
- Ubiquity matters: a protected channel the source already uses beats a better one they will not install

## 5. Cons

- Requires a phone number, which is an identifier the source must reveal to you and to Signal — a real limitation when the source must not be identifiable at all, and the reason SecureDrop exists
- Metadata minimisation is strong but not absolute: Signal knows when accounts registered and, to a limited degree, when they connect, and the operator is subject to legal process (its published transparency responses show it holds very little)
- Centralised service dependency: if Signal is blocked in a country, sources need censorship circumvention, and that adds operational burden exactly where it is hardest
- Safety-number verification is the step that makes end-to-end encryption meaningful against interception, and almost nobody does it — a training rather than a software problem

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 29,652 stars with 491 open issues, release v8.35.2 (2026-11-09), pushed 2026-11-16, AGPL-3.0; the server (signalapp/Signal-Server, AGPL-3.0, pushed 2026-11-16) is also published, which is unusual and supports the privacy claims. The protocol's cryptographic review record is extensively documented in published literature.

## 7. Assessment

Adopt as the default communication channel and train safety-number verification, because unverified end-to-end encryption protects against the wrong threat. For your profile the phone-number requirement is the decision point: use Signal for ongoing contact with sources whose identity you already know, and SecureDrop or Hush Line for first contact with sources who must stay anonymous. In exile contexts, plan for Signal being blocked — pre-arrange circumvention and a fallback channel before it is needed.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v8.35.2 (2026-11-09), tag v8.36.2, 29,652 stars, 491 open issues. Frequent releases under a funded non-profit; the server component is separately published and equally current.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0 on client and server. Note that running a modified client against Signal's servers is contrary to the service's terms regardless of the licence — relevant to forks like Molly.

**Licence evidence:** https://github.com/signalapp/Signal-Android/blob/main/LICENSE

## 10. Costs

Free to use. No infrastructure. Cost is training time and the operational work of maintaining circumvention where Signal is blocked.

## 11. Privacy and data flows

End-to-end encrypted content with strong metadata minimisation, backed by a published server implementation and a transparency record showing very little retained data. The irreducible disclosure is the phone number, which is an identifier linking source to journalist.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Requires a phone number — unsuitable where the source must not be identifiable

## 13. Alternatives

- [SimpleX Chat](SUR-B3-25.md) where no identifier at all can be exchanged
- [Molly](SUR-B3-24.md) for a hardened Signal-compatible Android client
- [SecureDrop](SUR-B3-01.md) or Hush Line for anonymous first contact

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/signalapp/Signal-Android
- https://github.com/signalapp/Signal-Server
- https://github.com/signalapp/Signal-Android/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 2 | [mat2](SUR-B3-07.md) | 94 | Adopt |
| 3 | [SecureDrop](SUR-B3-01.md) | 92 | Adopt |
| 4 | [CryptPad](SUR-B3-27.md) | 92 | Adopt |
| 5 | [Dangerzone](SUR-B3-03.md) | 92 | Adopt |
| 6 | [OnionShare](SUR-B3-04.md) | 92 | Adopt |
| 7 | [Orbot](SUR-B3-30.md) | 92 | Adopt |
| 8 | [Tails](SUR-B3-19.md) | 92 | Adopt |
| 9 | [MVT (Mobile Verification Toolkit)](SUR-B3-08.md) | 90 | Adopt |

---

← 4. [Scrapy](OSINT-C1-16.md) · 6. [yt-dlp](OSINT-C1-45.md) →
