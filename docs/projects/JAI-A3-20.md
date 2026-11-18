# Sigstore Cosign

`JAI-A3-20` · **77/100** · overall rank 193 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 79) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 13) |
| **Subcategory** | Supply-chain provenance |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Sigstore project (OpenSSF) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/sigstore/cosign) · [Documentation](https://docs.sigstore.dev/cosign/overview/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 3/5 · licence+cost 5/5 → **weighted 77/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. The public Sigstore infrastructure is free to use. Cost is engineering time to add verification to deployment. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/sigstore/cosign/blob/main/LICENSE
- https://github.com/sigstore/cosign
- https://docs.sigstore.dev/cosign/overview/

---

## 1. Purpose

Tool for signing, verifying and storing signatures for container images and other software artefacts, with keyless signing via OIDC identity and transparency-log recording.

## Journalism / investigative use case

Verifying what you deploy and attesting what you publish: signature verification on the container images running your SecureDrop, archive or analysis infrastructure, and signed attestations for datasets you release so downstream users can confirm they came from you unmodified.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Addresses a real and ignored risk: a newsroom running unverified container images in its source-protection path is trusting whatever a registry served, and signature verification closes that
- Keyless signing via OIDC removes the key-management burden that otherwise prevents signing from happening at all — the practical reason most organisations do not sign anything
- Transparency-log recording means signatures are publicly auditable, so a tampered artefact is detectable rather than merely unsigned
- Apache-2.0 under OpenSSF governance with very active maintenance (v3.1.4, 2026-10-20; pushed 2026-11-16) and strong adoption (6,444 stars)

## 5. Cons

- Keyless signing records an identity in a public transparency log, which for a newsroom signing artefacts means publishing an organisational identity — usually fine, occasionally a consideration
- Verification only helps if you actually enforce it in deployment, and adding policy enforcement to a deployment pipeline is the work most teams skip after installing the tool
- Container-and-artefact oriented, so it addresses software supply chain rather than document or media provenance (C2PA covers that)
- Concepts (attestations, transparency logs, OIDC identities) take orientation for a team without supply-chain security background

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 6,444 stars with release v3.1.4 (2026-10-20), pushed 2026-11-16, Apache-2.0 under OpenSSF governance. Sigstore's adoption across major open-source ecosystems is well documented and is why signature verification is now practical.

## 7. Assessment

Worth integrating into deployment for the specific infrastructure that protects sources — if you run SecureDrop, an archive or a document pipeline from container images, verifying signatures is a cheap, meaningful hardening step. For your profile the second use is also worth considering: signing datasets and document releases so partners and readers can verify they came from you unaltered, which pairs with C2PA for media and matters when your work is republished or misattributed.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v3.1.4 (2026-10-20), 6,444 stars, Apache-2.0. Regular releases under OpenSSF governance with broad industry participation.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material.

**Licence evidence:** https://github.com/sigstore/cosign/blob/main/LICENSE

## 10. Costs

No fee. The public Sigstore infrastructure is free to use. Cost is engineering time to add verification to deployment. Estimate.

## 11. Privacy and data flows

Keyless signing records your signing identity in a public transparency log, which is a deliberate disclosure. Verification itself contacts the transparency log, revealing what you are verifying — minor, but worth knowing for an air-gapped deployment, where offline verification with keys is the alternative.

## 12. Verdict

**Integrate**

## 13. Alternatives

- Traditional GPG signing with your own keys, avoiding the transparency-log disclosure at the cost of key management
- C2PA for media and document provenance rather than software artefacts
- Pinning image digests, which gives immutability without authenticity

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/sigstore/cosign
- https://docs.sigstore.dev/cosign/overview/
- https://github.com/sigstore/cosign/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [llama.cpp](JAI-A3-01.md) | 96 | Adopt |
| 2 | [Ollama](JAI-A3-02.md) | 94 | Adopt |
| 3 | [vLLM](JAI-A3-03.md) | 90 | Adopt |
| 4 | [Haystack](JAI-A3-05.md) | 85 | Adopt |
| 5 | [llm (Simon Willison's CLI)](JAI-A3-12.md) | 85 | Adopt |
| 6 | [promptfoo](JAI-A3-14.md) | 85 | Adopt |
| 7 | [RAGFlow](JAI-A3-06.md) | 85 | Pilot |
| 8 | [LlamaIndex](JAI-A3-04.md) | 82 | Pilot |

---

← 192. [openstates-scrapers](OSINT-C3-13.md) · 194. [Subtitle Edit](JAI-A2-50.md) →
