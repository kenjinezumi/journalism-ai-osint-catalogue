# Tor Browser Launcher

`SUR-B3-29` · **80/100** · overall rank 157 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 43) |
| **Segment** | B3 · Protecting journalists and sources (rank 25) |
| **Subcategory** | Anonymous browsing |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Tor Project (transferred from micahflee) |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/torproject/torbrowser-launcher) · [Documentation](https://torproject.org/download/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 5/5 · licence+cost 5/5 → **weighted 80/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a. Tor Browser itself is separately licensed (predominantly MPL-2.0 and BSD-family, as a Firefox derivative). |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Free. No infrastructure.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/torproject/torbrowser-launcher/blob/main/LICENSE
- https://github.com/torproject/torbrowser-launcher
- https://torproject.org/download/
- `../sources/evidence/leads.md`

---

## 1. Purpose

Linux helper that downloads, verifies the signature of, installs and launches Tor Browser, keeping it updated and integrating it into the desktop.

## Journalism / investigative use case

Getting Tor Browser onto reporters' Linux machines with signature verification done correctly — because the step people skip is verification, and an unverified Tor Browser download is precisely the attack a hostile network operator would mount against a journalist.

## 2. Audience

journalist, engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Automates GPG signature verification, which is the security-critical step that manual downloaders omit — this is the tool's real contribution
- Keeps Tor Browser updated, and an outdated Tor Browser is a meaningful risk given that browser exploits are the standard route to deanonymisation
- MIT licensed and now maintained under the Tor Project organisation (transfer from micahflee verified by redirect in this session), which is a governance improvement
- Packaged in major Linux distributions, so installation is usually a single package-manager command

## 5. Cons

- Release metadata is stale (v0.3.7 from 2024-01-28 against tag v0.3.9), so the published release lags the tag line and version tracking is awkward for a security tool
- 89 open issues against 890 stars, and the launcher is a thin wrapper whose own bugs can block updates — an ironic failure mode for an updater
- Linux only; Windows and macOS users download Tor Browser directly and must verify manually, so this solves the problem for only part of a mixed team
- Using Tor at all can be conspicuous on a monitored network, which the launcher does nothing to address — bridges must be configured separately

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 890 stars with 89 open issues, release v0.3.7 (2024-01-28), tag v0.3.9, pushed 2026-11-05, MIT licence; the repository transfer micahflee/torbrowser-launcher → torproject/torbrowser-launcher was confirmed by API redirect on 2026-11-17 and recorded in leads.md L4.

## 7. Assessment

Use it on Linux and, more importantly, make signature verification a trained habit for everyone regardless of platform — that is the transferable lesson. For your profile the operational points are: install from your distribution's package where possible, check that updates are actually arriving (a stalled launcher silently leaves an old browser in place), and pre-configure bridges for anyone working where Tor is blocked or monitored.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-05, latest release v0.3.7 (2024-01-28), tag v0.3.9, 890 stars, 89 open issues. Commits within the last two weeks but no release in nearly three years; a thin, stable wrapper now under Tor Project stewardship. Classified stable-low because the release gap is real for a security-adjacent tool.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a. Tor Browser itself is separately licensed (predominantly MPL-2.0 and BSD-family, as a Firefox derivative).

**Restrictions:** None material.

**Licence evidence:** https://github.com/torproject/torbrowser-launcher/blob/main/LICENSE

## 10. Costs

Free. No infrastructure.

## 11. Privacy and data flows

The launcher itself contacts the Tor Project to download and verify the browser, which is unremarkable, though on a monitored network that download is visible. Tor Browser then provides the anonymity properties.

## 12. Verdict

**Integrate**

## 13. Alternatives

- Direct download from torproject.org with manual GPG verification (required on Windows and macOS)
- [Tails](SUR-B3-19.md), which bundles a verified Tor Browser in an amnesic environment
- [Orbot](SUR-B3-30.md) for routing Android traffic through Tor

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/torproject/torbrowser-launcher
- https://torproject.org/download/
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

← 156. [name-variant-search](OSINT-C1-12.md) · 158. [FAISS](JAI-A3-08.md) →
