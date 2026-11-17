# Orbot

`SUR-B3-30` · **92/100** · overall rank 27 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 9) |
| **Segment** | B3 · Protecting journalists and sources (rank 7) |
| **Subcategory** | Anonymous networking (mobile) |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Guardian Project |
| **Maintenance** | Actively maintained |
| **Licence** | Not detected by the GitHub API — read the repository licence file (Guardian Project projects are predominantly BSD/GPL-family) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/guardianproject/orbot-android) · [Documentation](https://orbot.app/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 92/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Android application that provides Tor connectivity for the device, either as a VPN-mode tunnel for selected applications or system-wide, with bridge support for censored networks.

## Journalism / investigative use case

Routing a reporter's phone traffic through Tor in a country where the network is monitored or specific services are blocked — including selectively tunnelling only the applications that matter, so a messaging app works while ordinary traffic looks normal.

## 2. Audience

journalist, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Per-application tunnelling is the practically important feature: routing everything through Tor is slow and conspicuous, while tunnelling just the messaging or browsing app is usable daily
- Bridge support addresses the case that actually matters — networks where Tor itself is blocked — which is common in the jurisdictions exile media report on
- Very actively maintained (release 17.9.8-RC-1 with Tor 0.4.9.17 on 2026-11-16; pushed the same day) by Guardian Project, which has a long record in this field
- Repository transfer guardianproject/orbot → guardianproject/orbot-android verified by redirect, so the canonical path is current

## 5. Cons

- VPN-mode Tor on Android is visible to anyone inspecting the device, and in some jurisdictions the presence of Orbot is itself incriminating — a risk the app cannot mitigate
- Tor over mobile networks is slow and battery-hungry, so users disable it exactly when they are travelling and most at risk
- GitHub reports SPDX NOASSERTION so the licence must be read from the repository, and the release/tag structure is confusing (RC releases against a v15-beta-2 tag)
- Mobile Tor does not protect against application-level identifiers: an app that transmits an account identity over Tor is still identified

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 3,711 stars with 87 open issues, release 17.9.8-RC-1-tor-0.4.9.17 (2026-11-16) with same-day push, SPDX NOASSERTION; the repository is mirrored from Guardian Project's GitLab. Transfer confirmed by API redirect 2026-11-17.

## 7. Assessment

Adopt for reporters working in censored or monitored networks, with per-app tunnelling rather than system-wide so it stays usable. For your profile the briefing that matters is twofold: configure bridges before travel rather than on arrival, and be clear that Tor hides the network path, not the account you log into — a journalist signing into an identified account over Tor has protected very little. In jurisdictions where Orbot's presence is itself risky, consider whether a clean device is the better answer.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release 17.9.8-RC-1-tor-0.4.9.17 published the same day, 3,711 stars, 87 open issues. Same-day release and push, tracking current Tor versions, under a long-established maintainer.

## 9. Licensing

**Licence:** Not detected by the GitHub API — read the repository licence file (Guardian Project projects are predominantly BSD/GPL-family) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Unverified in this survey; confirm from the repository before redistribution.

**Licence evidence:** https://github.com/guardianproject/orbot-android

## 10. Costs

Free. No infrastructure. Cost is battery life and connection speed for the user.

## 11. Privacy and data flows

Provides network-level anonymity for tunnelled applications, with bridges for censored networks. Residual risks: app presence is visible on the device, application-level identifiers defeat network anonymity, and mobile-network metadata (that the phone connected at all, and from which cell) is unaffected.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Presence of the app may itself be incriminating in some jurisdictions

## 13. Alternatives

- Tor Browser for Android where only browsing needs protection
- [Outline](SUR-B3-31.md) or a trusted VPN where the goal is circumvention rather than anonymity
- A clean, separately provisioned device for the highest-risk travel

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/guardianproject/orbot-android
- https://orbot.app/
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
| 8 | [Tails](SUR-B3-19.md) | 92 | Adopt |
| 9 | [MVT (Mobile Verification Toolkit)](SUR-B3-08.md) | 90 | Adopt |

---

← 26. [OnionShare](SUR-B3-04.md) · 28. [Tails](SUR-B3-19.md) →
