# SpyGuard

`SUR-B3-12` · **76/100** · overall rank 200 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 55) |
| **Segment** | B3 · Protecting journalists and sources (rank 29) |
| **Subcategory** | Network-based spyware detection |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | SpyGuard project (fork of Kaspersky's TinyCheck) |
| **Maintenance** | Stable with low activity |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/SpyGuard/SpyGuard) · [Documentation](https://github.com/SpyGuard/SpyGuard#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 76/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Indicator sets come from third-party sources with their own terms. |
| **Restrictions** | None material — a clean OSI licence, which is a notable contrast with MVT in the same workflow. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Dedicated hardware; self-hosted infrastructure |
| **Cost conditions** | Dedicated hardware; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Hardware: a Raspberry Pi class device with two network interfaces plus a screen or remote access (low hundreds in hardware, estimate). Build and maintenance time for the appliance.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/SpyGuard/SpyGuard/blob/main/LICENSE
- https://github.com/SpyGuard/SpyGuard
- `../sources/evidence/leads.md`

---

## 1. Purpose

Appliance-style tool that creates a Wi-Fi access point, captures a device's network traffic and analyses it against indicators of compromise to detect spyware communication, without installing anything on the device.

## Journalism / investigative use case

Non-invasive device screening: a journalist connects their phone to a SpyGuard access point for a few minutes and the traffic is analysed for known spyware command-and-control communication — no backup, no ADB, nothing installed, which makes it usable in a workshop or a field setting where MVT's acquisition is impractical.

## 2. Audience

specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Requires nothing on the device, which is a genuine advantage for consent, speed and for devices you cannot or should not back up — a workshop can screen a dozen phones in an hour
- Network-level detection catches active communication that an on-device check might miss, so it is complementary to MVT rather than duplicative
- Apache-2.0 — a clean OSI licence, notably unlike MVT's consensual-use restriction, so there is no licensing complication
- Fork of Kaspersky's TinyCheck (whose original repository is now a 404, verified in this session), so this is the surviving maintained line of a well-regarded design

## 5. Cons

- Only detects spyware that communicates during the capture window, so a dormant implant or one using a novel endpoint is invisible — a clean result is weak evidence
- Indicator-dependent like all such tooling, and the indicator sets age
- Requires dedicated hardware (a Raspberry Pi class device with two network interfaces) and setup, so it is an appliance to build rather than software to install
- Slowing cadence: release v2.1 and last push both 2026-06-16, five months before this survey, with 514 stars and 13 open issues

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 514 stars with 13 open issues, release v2.1 (2026-06-16) with the last push the same day, Apache-2.0. Its lineage from Kaspersky's TinyCheck is stated by the project, and the original KasperskyLab/TinyCheck path returns a 404 (verified 2026-11-17) — making SpyGuard the available implementation.

## 7. Assessment

Worth building as an appliance if you run digital-security workshops or support journalists in the field — the non-invasive screening model fits those settings far better than MVT. For your profile I would treat it as triage rather than examination: a hit justifies a full MVT examination, and a clean result justifies nothing beyond 'no known spyware communicated in those minutes'. Keep the indicator sets updated and note the slowing maintenance as a monitoring item.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-06-16, latest release v2.1 published the same day, 514 stars, 13 open issues. Five months since any activity on a security tool whose value depends on current indicators — a real caveat, though the project is complete rather than abandoned.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** Indicator sets come from third-party sources with their own terms.

**Restrictions:** None material — a clean OSI licence, which is a notable contrast with MVT in the same workflow.

**Licence evidence:** https://github.com/SpyGuard/SpyGuard/blob/main/LICENSE

## 10. Costs

No fee. Hardware: a Raspberry Pi class device with two network interfaces plus a screen or remote access (low hundreds in hardware, estimate). Build and maintenance time for the appliance.

## 11. Privacy and data flows

Traffic capture happens on your appliance and stays there; nothing is sent to a vendor. The captured traffic is highly sensitive (it is the person's live network activity), so retention should be minimal and consent explicit even though the licence does not compel it.

## 12. Verdict

**Pilot**

## 13. Alternatives

- MVT for a deeper on-device examination
- Pi-hole or a manual pcap plus indicator matching for a do-it-yourself equivalent
- Referral to Access Now's Digital Security Helpline for individual cases

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/SpyGuard/SpyGuard
- https://github.com/SpyGuard/SpyGuard/blob/main/LICENSE
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

← 199. [Helsinki-NLP OPUS-MT](JAI-A2-21.md) · 201. [news-homepages](JAI-A1-31.md) →
