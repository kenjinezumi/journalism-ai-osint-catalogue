# asn (nitefood)

`OSINT-C3-27` · **72/100** · overall rank 247 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 84) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 26) |
| **Subcategory** | Network attribution |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | nitefood |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT (project licensing — confirm from the repository licence file) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/nitefood/asn) · [Documentation](https://github.com/nitefood/asn#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 3/5 · usability 4/5 · licence+cost 5/5 → **weighted 72/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT (project licensing — confirm from the repository licence file) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Third-party data sources have their own terms; RIR data is generally open. |
| **Restrictions** | Permissive as published; third-party service terms apply to automated querying. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. Negligible compute. Some data sources may rate-limit or require keys.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/nitefood/asn

---

## 1. Purpose

Shell-based reconnaissance tool that resolves IP addresses, prefixes, ASNs and domains to network ownership, BGP routing, geolocation and reputation data, with bulk and interactive modes.

## Journalism / investigative use case

Answering 'who owns this address' quickly and from several sources: given an IP from a log, a certificate or a leaked document, establish the hosting provider, the announcing ASN and the responsible organisation — the attribution step that turns a technical artefact into a nameable entity.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Aggregates several authoritative sources (RIR records, BGP data, geolocation) in one command, which is faster and less error-prone than consulting each by hand
- Bulk mode means you can attribute a list of addresses from a log or a dataset in one pass, which is the realistic investigative need
- Shell-based with no heavy dependencies, so it runs anywhere including a minimal container or a field machine
- Covers the authoritative sources that matter for a published attribution claim (RIR allocation and BGP announcement) rather than only commercial geolocation

## 5. Cons

- Queries go to multiple third-party services, so your target addresses are disclosed to several providers — worth routing through a dedicated egress
- IP geolocation is notoriously imprecise at city level and worse for mobile and cloud ranges, so a published location claim based on it is fragile
- Shell-script architecture means error handling is basic and output parsing for automation is awkward
- Small project; verify liveness and source availability before relying on it for a deadline

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived. The tool is known in the network-investigation community as a convenient aggregator; no journalism deployment verified.

## 7. Assessment

Integrate it as the quick attribution step, with the discipline of confirming anything published against the RIR record directly — allocation data is authoritative and geolocation is not. For your profile the common error to avoid is publishing an IP geolocation as a location: for cloud and mobile addresses it is frequently wrong by hundreds of kilometres, and the defensible claim concerns who announces and who was allocated the range, not where a server physically sits.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived with modest ongoing activity. Classified stable-low; because the capability depends on third-party source availability, verify it works before relying on it.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Third-party data sources have their own terms; RIR data is generally open.

**Restrictions:** Permissive as published; third-party service terms apply to automated querying.

**Licence evidence:** https://github.com/nitefood/asn

## 10. Costs

No fee. Negligible compute. Some data sources may rate-limit or require keys.

## 11. Privacy and data flows

Queries disclose the addresses and domains you are investigating to several third-party services — more exposure than a single lookup, so use a dedicated egress for sensitive work.

## 12. Verdict

**Integrate**

## 13. Alternatives

- Direct RIR (RIPE, ARIN, APNIC) queries for authoritative allocation data
- PyBGPStream for rigorous BGP analysis from public archives
- [Metabigor](OSINT-C1-09.md) for organisation-level netblock and ASN mapping

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/nitefood/asn

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OpenSanctions (dataset)](OSINT-C3-01.md) | 94 | Adopt |
| 2 | [Uwazi](OSINT-C3-05.md) | 94 | Adopt |
| 3 | [Tella](OSINT-C3-06.md) | 89 | Adopt |
| 4 | [NetworkX](OSINT-C3-31.md) | 88 | Adopt |
| 5 | [Quarto](OSINT-C3-39.md) | 85 | Adopt |
| 6 | [CourtListener](OSINT-C3-11.md) | 84 | Adopt |
| 7 | [Querido Diário](OSINT-C3-14.md) | 83 | Integrate |
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |

---

← 246. [olmOCR](JAI-A2-34.md) · 248. [Klaxon (self-hosted)](SUR-B1-18.md) →
