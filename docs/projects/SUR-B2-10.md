# certstream-server

`SUR-B2-10` · **78/100** · overall rank 173 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 48) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 11) |
| **Subcategory** | Certificate transparency monitoring |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Cali Dog Security |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/CaliDog/certstream-server) · [Documentation](https://certstream.calidog.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 3/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 78/100**

---

## 1. Purpose

Server that aggregates certificate-transparency logs into a real-time stream of newly issued TLS certificates, with a websocket API for consumers.

## Journalism / investigative use case

Watching a surveillance vendor's infrastructure appear in real time: new certificates reveal new subdomains and hostnames as they are provisioned, so you learn about a new command-and-control domain, a new product environment or a renamed service before it is announced — and entirely passively, with no contact with the target.

## 2. Audience

engineer, specialist investigator

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Passive by construction: certificate-transparency logs are public and reading them involves no interaction with the target, which is the ideal operational-security profile for monitoring an adversary
- Real-time notification of new infrastructure is a genuine early-warning capability — infrastructure appears in CT logs before it appears anywhere else
- Self-hostable, so your monitoring interests are not disclosed to a service operator
- Underpins much of the certificate-monitoring tooling in this field, so understanding it explains the category

## 5. Cons

- High-volume stream: certificate issuance across the web is enormous, so useful monitoring requires filtering logic and storage design rather than just connecting
- Self-hosting means consuming and processing a very large data flow, which is real infrastructure; using a public CertStream instance discloses nothing directly but makes you dependent on its continuity
- Certificates reveal hostnames, not ownership, so attribution still requires registry and WHOIS work
- Maintenance cadence is modest and the project is small relative to its importance in the ecosystem

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived. Certificate-transparency monitoring is a well-established technique in both security research and open-source investigation, and CertStream is its best-known open implementation.

## 7. Assessment

Integrate it if you monitor specific adversaries over time — for a surveillance-industry beat, a filtered CT feed on a vendor's known domains is one of the highest-value, lowest-risk monitoring capabilities you can build. For your profile the practical design is to consume a public stream (or self-host if volume and privacy justify it), filter on a watchlist of domain patterns, and alert into an internal channel. Pair with Metabigor or RIR lookups for the ownership question that certificates cannot answer.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived, with modest activity. The project is a mature piece of infrastructure in a niche where the underlying data source (CT logs) is externally guaranteed, so low code velocity carries less risk than it would elsewhere.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Certificate-transparency log data is public by design.

**Restrictions:** Permissive as published. CT log data carries no usage restriction of consequence.

**Licence evidence:** https://github.com/CaliDog/certstream-server

## 10. Costs

No fee. Self-hosting estimate: sustained bandwidth and processing for a high-volume stream plus storage for whatever you retain — a real but modest infrastructure commitment; filtering at ingest keeps it small. Assumptions: watchlist-filtered retention rather than full archival.

## 11. Privacy and data flows

Entirely passive with respect to the target: reading CT logs involves no contact with the monitored infrastructure. Self-hosting also keeps your watchlist private, which a public-stream consumer with server-side filtering would not.

## 12. Verdict

**Integrate**

## 13. Alternatives

- crt.sh for interactive certificate searches without running infrastructure
- Commercial CT monitoring services, which are easier and disclose your watchlist
- [dnstwist](OSINT-C3-25.md) for detecting lookalike domains rather than monitoring known ones

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/CaliDog/certstream-server
- https://certstream.calidog.io/

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [mitmproxy](SUR-B2-06.md) | 96 | Adopt |
| 2 | [MobSF (Mobile Security Framework)](SUR-B2-04.md) | 88 | Adopt |
| 3 | [Citizen Lab publication directory](SUR-B2-20.md) | 86 | Reference only |
| 4 | [Exodus Privacy](SUR-B2-01.md) | 86 | Adopt |
| 5 | [USAspending.gov (custom award data)](SUR-B2-14.md) | 86 | Adopt |
| 6 | [Apktool](SUR-B2-05.md) | 86 | Adopt |
| 7 | [TED — Tenders Electronic Daily (EU public procurement)](SUR-B2-13.md) | 84 | Adopt |
| 8 | [DuckDuckGo Tracker Radar](SUR-B2-03.md) | 82 | Reference only |

---

← 172. [Surya](JAI-A2-52.md) · 174. [OpenSecrets lobbying data](SUR-B2-17.md) →
