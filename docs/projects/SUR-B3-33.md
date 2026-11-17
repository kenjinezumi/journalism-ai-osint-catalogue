# Privacy Badger

`SUR-B3-33` · **81/100** · overall rank 147 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 40) |
| **Segment** | B3 · Protecting journalists and sources (rank 23) |
| **Subcategory** | Tracking protection |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Electronic Frontier Foundation |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-family per EFF's licensing (GitHub reports NOASSERTION — read the repository licence file for records) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/EFForg/privacybadger) · [Documentation](https://privacybadger.org/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 5/5 · privacy 4/5 · usability 5/5 · licence+cost 4/5 → **weighted 81/100**

---

## 1. Purpose

Browser extension that learns to block third-party trackers by observing cross-site tracking behaviour rather than relying solely on blocklists, and removes outgoing link tracking and some fingerprinting vectors.

## Journalism / investigative use case

Reducing the trail a journalist leaves while researching: visiting a target's website, a procurement portal or an extremist forum would otherwise notify a dozen analytics and ad-tech companies, building a profile that associates your newsroom with the subjects you are investigating.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Behavioural learning catches trackers that blocklists miss, which matters on the obscure regional and niche sites investigations actually visit — exactly where curated lists have gaps
- Addresses a genuine and under-appreciated operational-security problem: research browsing builds a commercially held profile linking your organisation to your subjects
- Maintained by EFF with a current release (release-2026.9.15, 2026-09-15; pushed 2026-11-12) and a clear institutional mission
- Free, trivial to deploy across a newsroom, and requires no user discipline once installed

## 5. Cons

- Breaks some sites, and a journalist on deadline will disable it rather than diagnose it — so deployment needs a quick 'disable for this site' habit taught alongside it
- Blocking trackers does not hide you from the site you are visiting, which still sees your IP and request — for that you need Tor or a separate egress, and users conflate the two
- GitHub reports SPDX NOASSERTION (EFF's licensing is GPL-family) so the licence needs reading for records
- Behavioural learning means protection improves over time per profile, so a fresh browser profile starts weaker — relevant if reporters use disposable profiles for research

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 3,889 stars with 102 open issues, release release-2026.9.15 (2026-09-15), pushed 2026-11-12, SPDX NOASSERTION. EFF's maintenance and the behavioural-learning approach are documented by the project.

## 7. Assessment

Adopt it newsroom-wide — it is free, requires nothing of users, and reduces a real exposure. For your profile the important framing is that it addresses third-party tracking, not visibility to the site itself: a reporter researching a surveillance vendor should use a separate browser profile and a non-newsroom egress as well, because the vendor's own server logs are the more consequential record. Teach the per-site disable so people do not switch it off globally.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-12, latest release release-2026.9.15 (2026-09-15), 3,889 stars, 102 open issues, SPDX NOASSERTION. Regular dated releases under EFF's institutional maintenance.

## 9. Licensing

**Licence:** GPL-family per EFF's licensing (GitHub reports NOASSERTION — read the repository licence file for records) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Unverified exactly in this survey; immaterial for use as a browser extension.

**Licence evidence:** https://github.com/EFForg/privacybadger

## 10. Costs

Free. No infrastructure.

## 11. Privacy and data flows

Blocks third-party tracking locally in the browser with no data sent to EFF. It does not conceal you from the visited site, which is the limitation to communicate clearly.

## 12. Verdict

**Adopt**

## 13. Alternatives

- uBlock Origin for broader blocklist-based blocking
- Tor Browser where the visited site must not learn who you are
- A dedicated research browser profile with a separate egress for sensitive targets

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/EFForg/privacybadger
- https://privacybadger.org/

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

← 146. [Timesketch](OSINT-C3-37.md) · 148. [streetlevel](OSINT-C2-32.md) →
