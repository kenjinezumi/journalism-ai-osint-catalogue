# Sherloq

`OSINT-C2-12` · **80/100** · overall rank 153 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 50) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 22) |
| **Subcategory** | Image forensics workbench |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Guido Bartoli |
| **Maintenance** | Stable with low activity |
| **Licence** | GPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/GuidoBartoli/sherloq) · [Documentation](https://github.com/GuidoBartoli/sherloq#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 3/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 80/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a — classical signal-processing techniques, no trained models. |
| **Restrictions** | GPL-3.0; immaterial for desktop use by analysts. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Staff effort |
| **Cost conditions** | Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Runs on an analyst workstation; ExifTool binary and OpenCV required. Real cost is analyst training to interpret the outputs responsibly.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/GuidoBartoli/sherloq/blob/master/LICENSE
- https://github.com/GuidoBartoli/sherloq

---

## 1. Purpose

Desktop GUI aggregating a wide set of image-forensics techniques — metadata inspection, error-level analysis, noise and JPEG-ghost maps, clone/copy-move detection, PCA and frequency analysis — in one local workbench.

## Journalism / investigative use case

A single local workbench to triage a suspicious photo: pull metadata, look for ELA, noise and JPEG-ghost anomalies, test for copy-move or splicing, and build a documented list of anomalies to take to further reporting — all without uploading the image anywhere.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Breadth of techniques in one local GUI is the practical advantage: an analyst can run eight different tests in ten minutes rather than installing eight research repos
- Fully local with no third-party service or API key documented, which matters enormously for unpublished or source-supplied imagery — the direct contrast with the InVID plugin's uploads
- Largest community of any dedicated image-forensics GUI here (3,264 stars) with a modest backlog (25 open issues)
- GPL-3.0 and inspectable, so the methods are auditable rather than black-box

## 5. Cons

- The author frames it as an educational and research toolkit rather than a definitive forgery detector — every panel output is a probabilistic signal requiring expert interpretation, NOT conclusive proof
- ELA in particular is notoriously over-interpreted: it is the classic example of a forensic visualisation that looks compelling and proves little, and an analyst without training will produce false findings
- Last push 2026-07-16 with no releases at all, so there is no version to pin and the project runs on a maintainer's spare attention
- PySide2 and OpenCV dependencies of a certain vintage make installation fiddly on current systems

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 3,264 stars with 25 open issues, no releases, last push 2026-07-16; the author's own framing as an educational/research toolkit is stated in the repository. The over-interpretation risk of ELA is a well-established point in image-forensics literature, not a criticism specific to Sherloq.

## 7. Assessment

Adopt it as the local alternative to uploading images to a forensics service, with a firm internal rule: outputs are leads for an analyst, never findings for a story, and no ELA image is ever published as evidence. For your profile its real value is privacy plus breadth — it lets you examine source-supplied imagery without disclosure. Pair with CAT-Net for a commercially usable model-based second opinion, and be realistic that interpreting these panels well requires training you may need to arrange.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-07-16, no releases or tags, 3,264 stars, 25 open issues. Four months since last push on a single-maintainer GUI; low backlog suggests attention, absence of releases suggests informal maintenance. Not declining, but the bus factor is one.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a — classical signal-processing techniques, no trained models.

**Restrictions:** GPL-3.0; immaterial for desktop use by analysts.

**Licence evidence:** https://github.com/GuidoBartoli/sherloq/blob/master/LICENSE

## 10. Costs

No fee. Runs on an analyst workstation; ExifTool binary and OpenCV required. Real cost is analyst training to interpret the outputs responsibly.

## 11. Privacy and data flows

No third-party service or API key documented for the core tools; analysis runs locally, which is the decisive advantage for unpublished or source-sensitive imagery.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [PhotoHolmes](JAI-A4-17.md) for model-based localisation methods (with per-method licence caveats)
- [CAT-Net](JAI-A4-19.md) for a commercially usable splicing detector
- InVID plugin for speed on already-public images, accepting the uploads

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/GuidoBartoli/sherloq
- https://github.com/GuidoBartoli/sherloq/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [ExifTool](OSINT-C2-01.md) | 96 | Adopt |
| 2 | [geopandas](OSINT-C2-21.md) | 94 | Adopt |
| 3 | [PySceneDetect](OSINT-C2-10.md) | 94 | Adopt |
| 4 | [QGIS](OSINT-C2-19.md) | 91 | Adopt |
| 5 | [ShadowFinder](OSINT-C2-17.md) | 91 | Adopt |
| 6 | [MediaInfo](OSINT-C2-04.md) | 88 | Adopt |
| 7 | [osm-search](OSINT-C2-27.md) | 87 | Adopt |
| 8 | [GDAL](OSINT-C2-20.md) | 86 | Adopt |

---

← 152. [Presidio](JAI-A2-40.md) · 154. [Skyfield](OSINT-C2-38.md) →
