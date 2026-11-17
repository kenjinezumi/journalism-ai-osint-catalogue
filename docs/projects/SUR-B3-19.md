# Tails

`SUR-B3-19` · **92/100** · overall rank 28 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 10) |
| **Segment** | B3 · Protecting journalists and sources (rank 8) |
| **Subcategory** | Amnesic operating system |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Tails project (Tor Project affiliated) |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0-or-later (project licensing; the distribution aggregates many components under their own licences) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://gitlab.tails.boum.org/tails/tails) · [Documentation](https://tails.net/doc/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 92/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Live operating system booted from a USB stick that routes all network traffic through Tor, leaves no trace on the host computer by default, and bundles encryption, secure deletion and anonymity tooling.

## Journalism / investigative use case

The standard tool for working on sensitive material on a machine you do not trust, or for a source who must contact you without leaving evidence on their own computer: boot Tails, work, shut down, and the computer retains nothing. Also the historical environment for handling the most sensitive leaks.

## 2. Audience

journalist, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Amnesia by default is a structural protection no application can provide: nothing written to the host disk means nothing to find in a later device search
- All traffic forced through Tor removes the commonest operational-security mistake — a single application leaking outside the tunnel
- Actively maintained with a visible release cadence (Tails 7.17 announced on the project's news page, verified 2026-11-17) and a long institutional track record in press-freedom contexts
- Optional encrypted persistent storage lets a journalist keep keys and documents across sessions when amnesia is inconvenient, as an explicit choice

## 5. Cons

- Developed on the project's own GitLab rather than GitHub, so it is invisible to GitHub-based discovery and dependency tooling; the GitHub path TAILS-Project/TAILS is an unrelated stub (1 star, last push 2017) and must not be mistaken for it
- Booting from USB requires access to firmware settings, which managed, corporate or locked-down laptops often prevent — and in some countries carrying a Tails USB is itself incriminating
- Tor-only networking is slow and breaks many ordinary web services, so it is a dedicated-session tool rather than a daily environment
- Persistent storage, if enabled, reintroduces exactly the forensic trace that amnesia removes — a configuration choice with serious consequences that users make casually

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: Tails 7.17 is the most recent release announced on tails.net/news (retrieved 2026-11-17), and the project's own GitLab instance is the development home — the GitLab API on that host is not publicly queryable, so maintenance was verified from the release announcements instead. Tails's role in high-profile leak handling is extensively documented publicly.

## 7. Assessment

Adopt as a standard capability: keep prepared Tails USB sticks and train reporters to use them for first contact with unknown material and for work on untrusted machines. For your profile, two points matter particularly in exile contexts. First, possession can be a risk in itself — think about where sticks are stored and how they look. Second, decide a policy on persistence: amnesia is the protection, and a persistent volume full of documents on a USB stick in a journalist's bag is a different and worse threat model than they imagine.

## 8. Maintenance

**Actively maintained** — Release announcements on tails.net/news retrieved 2026-11-17 show Tails 7.17 as the current release, with the 7.x line in active development. Development occurs on gitlab.tails.boum.org (API not publicly queryable, so repository-level metrics are unavailable). The unrelated GitHub stub TAILS-Project/TAILS (1 star, pushed 2017-10-20) is NOT the project and should not be cited.

## 9. Licensing

**Licence:** GPL-3.0-or-later (project licensing; the distribution aggregates many components under their own licences) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. The distribution bundles software under many licences.

**Restrictions:** Aggregate free-software licensing; immaterial for use. Redistribution of a modified Tails image would require attention to the component licences.

**Licence evidence:** https://tails.net/doc/about/license/

## 10. Costs

No fee. A USB stick per user (negligible) plus the time to prepare and verify images. Verification of the download signature is an essential, non-optional step and takes a few minutes.

## 11. Privacy and data flows

The strongest privacy posture available in a general-purpose environment: no host disk writes, all traffic over Tor, memory wiped on shutdown. Residual risks are physical (possession of the stick), firmware-level compromise of the host, and user error in enabling persistence.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Requires firmware access to boot from USB; possession may itself carry risk in hostile jurisdictions

## 13. Alternatives

- [Qubes OS](SUR-B3-20.md) for a compartmentalised daily-use system rather than an amnesic session
- A dedicated air-gapped laptop for the most sensitive material
- Whonix for Tor-routed virtual machines on an existing host

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `docs-reviewed`

- https://tails.net/doc/
- https://tails.net/news/index.en.html
- https://gitlab.tails.boum.org/tails/tails

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
| 9 | [MVT (Mobile Verification Toolkit)](SUR-B3-08.md) | 90 | Adopt |

---

← 27. [Orbot](SUR-B3-30.md) · 29. [QGIS](OSINT-C2-19.md) →
