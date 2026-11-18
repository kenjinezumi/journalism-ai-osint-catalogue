# Methodology

How the 361 projects in this catalogue were found, verified, assessed and scored — and what the
results do not establish.

## Scope

Three research areas, split into ten segments so that rankings stay comparable within a
subcategory:

| Pillar | Segments |
|---|---|
| **Journalism and AI** | A1 discovery, scraping, ingestion, data journalism, newsroom workflow · A2 documents and language (OCR, transcription, translation, entities, entity resolution) · A3 RAG, research agents, knowledge graphs, provenance, AI evaluation · A4 fact-checking support and media verification |
| **Surveillance and journalist protection** | B1 monitoring public information, narratives, disinformation, censorship, harassment · B2 investigating surveillance companies, infrastructure, procurement, tracking technologies · B3 protecting journalists and sources |
| **OSINT and digital investigations** | C1 web and social research, archives, evidence capture · C2 image and video verification, geolocation, satellite, aviation, maritime · C3 public records, corporate ownership, finance, internet infrastructure, link analysis, collaboration |

Each project appears in exactly **one** segment, chosen by primary role, so no project is counted
twice. General-purpose components are included only where a concrete journalism or investigative
use case is stated in the assessment.

Projects are labelled by what they actually are, in the `bucket` field:

| Bucket | Meaning |
|---|---|
| `verified-oss` | OSI-approved or equivalently permissive licence, confirmed against the licence file or API metadata |
| `source-available-restricted` | Source is public but the licence restricts commercial, non-profit-only or field-of-use terms |
| `source-available-weights` | Code is open but model weights carry additional restrictions |
| `proprietary-service` | Hosted service or proprietary software, catalogued because it is a practical dependency |
| `uncertain` | Licence could not be confirmed; reuse treated as legally unresolved |

## Verification standard

**Verification dates: 2026-11-16** (inherited from the first research session and re-checked
here) and **2026-11-17** (this session's own checks). Every assessment records its own date.

What was actually done:

1. **Metadata sweep.** 583 candidate repositories were queried through the GitHub REST API on
   2026-11-17, capturing canonical `full_name` (which reveals renames, because REST follows
   redirects), SPDX licence, `archived`, `pushed_at`, latest release and tag, stars, open issues
   and fork parent. The raw output is committed at [`work/meta.jsonl`](../work/meta.jsonl) and is
   the primary maintenance evidence for most entries.
2. **Licence files read directly.** Every `NOASSERTION` result was resolved by reading the
   repository's own licence blob rather than left as "Other". Retrieved licence texts are
   committed under [`sources/evidence/licences/`](../sources/evidence/licences/). This is how
   three different causes of `NOASSERTION` were separated: a genuinely non-OSI licence, a
   standard licence with a prepended note, and a dataset licence rather than a software one.
3. **Redirects checked before calling a URL broken.** A 404 was only treated as broken after
   confirming there was no redirect. 17 candidate paths from the first session were genuine 404s
   and are listed with their real homes in
   [`sources/evidence/leads.md`](../sources/evidence/leads.md).
4. **Prices read from vendor pages**, with currency, billing period, basis and verification date
   recorded. Where a price was not publicly listed, it is recorded as "quote required" or
   "not verified" rather than estimated. See
   [`sources/evidence/pricing.md`](../sources/evidence/pricing.md).
5. **Source URLs verified.** Every candidate public-records URL was checked; a 403 to `curl` was
   recorded as bot protection rather than removal. See
   [`sources/evidence/b2-sources.md`](../sources/evidence/b2-sources.md).

### Assessment depth

Stated per project, and never overstated:

| Depth | Meaning |
|---|---|
| `metadata-verified` | API metadata plus documentation reviewed |
| `repo-inspected` | Repository contents or licence text read directly |
| `docs-reviewed` | Vendor or project documentation only (used for hosted services with no repository) |

**No project in this catalogue was installed or run.** No entry claims hands-on testing, and
capability judgements are inferences from documentation, repository inspection and metadata.

### Evidence confidence

Recorded separately from the score and never folded into it:

| Confidence | Meaning |
|---|---|
| **high** | Primary sources verified — licence file read, API metadata captured, official pricing page retrieved |
| **medium** | Official documentation or README reviewed; some fields inferred from reliable secondary sources |
| **low** | Limited or conflicting evidence; several fields unverified |

A project may be marked **provisional** where the evidence does not support a firm score. A
provisional entry still carries a numeric score for comparability, with the gap stated in its
Evidence section and in
[`docs/findings-and-limitations.md`](findings-and-limitations.md).

## Scoring rubric

The rubric was defined in the first research session and
[adopted unchanged](../sources/recovered/cat/RUBRIC.md) here, so that scores from both sessions
remain comparable. Each dimension is scored 0–5; the weighted total is
`sum(score ÷ 5 × weight)`, rounded to a whole number out of 100.

| Criterion | Weight | What it measures |
|---|--:|---|
| Journalism and workflow relevance | 30% | Fit to a reporting, investigation or source-protection workflow |
| Demonstrated capability and usefulness | 20% | Evidenced functional capability at useful scale |
| Maintenance, reliability and maturity | 15% | Substantive activity, releases, security process, institutional backing |
| Privacy and deployment control | 15% | Whether sensitive material can stay under your control |
| Usability, documentation and integration effort | 10% | Who can operate it, and at what cost in effort |
| Licensing and cost suitability | 10% | Actual impact of the licence and cost on a newsroom's intended use |

Band definitions for each dimension are in the
[rubric file](../sources/recovered/cat/RUBRIC.md). Three rules were applied throughout:

- **Popularity is not suitability.** Star counts are used as evidence about *maintenance*
  (particularly the open-issue-to-star ratio, which indicates triage) and never as a proxy for
  quality or fit.
- **Missing evidence is not scored as zero.** Where a dimension could not be evidenced, the
  assessment says so and the entry is marked provisional; dimensions are never silently
  reweighted.
- **Specialist tools are scored against their intended role.** A narrow tool that does one
  investigative job well is not penalised for narrowness, but relevance is capped by how often
  that job arises.

### Maintenance classification

Six states, with the reasoning stated per project. A recent push does not establish active
maintenance, and infrequent commits do not establish abandonment.

| State | Basis |
|---|---|
| **Actively maintained** | Substantive commits plus releases, issue throughput, or institutional backing with a security process |
| **Stable with low activity** | Mature and functionally complete; low change velocity is appropriate, not a penalty |
| **Maintenance appears to be declining** | Commits or releases have slowed materially against an open backlog, with no deprecation notice — the most hazardous state, because the project looks alive |
| **Dormant** | No substantive activity for an extended period; dependency rot likely |
| **Archived or discontinued** | `archived=true` on the API, or the upstream capability has been withdrawn |
| **Uncertain** | Maintenance cannot be evidenced — typically a hosted service with no public repository |

### Verdicts

| Verdict | Meaning |
|---|---|
| **Adopt** | Deploy it; the assessment states any conditions |
| **Integrate** | Worth building into a pipeline or stack as a component |
| **Pilot** | Promising, but evaluate on your own material before committing |
| **Monitor** | Not now; a specific change would alter the judgement |
| **Reference only** | Useful to read, cite or learn from, not to deploy |
| **Avoid for new deployment** | Do not build on it; a named alternative is given |

### Material blockers

Licence, dependency and operational-security problems that would stop a deployment are recorded
in a **separate field**, never folded into the score. 149 of 361 projects carry at least one.
A project can therefore score well and still be unusable for a particular organisation — the
score answers "how good is this for this kind of work", and the blocker answers "can you
actually use it".

## Classifying licences and costs

Licensing and payment are recorded as two separate questions, because conflating them produces
the two most common errors in tool selection: assuming that a permissive licence implies a free
service, and assuming that a free download implies permissive terms. Nothing in this catalogue
is treated as free because it is published on GitHub or because it can be self-hosted.

Each record carries six derived fields alongside its hand-written `licence` and `costs` prose:

| Field | What it records |
|---|---|
| `licence_type` | The classification of the recorded terms — permissive, weak or strong copyleft, dual-licensed, public domain, open data, mixed code-versus-weights/data, restricted non-OSI, proprietary, or unresolved |
| `oss_status` | What those terms permit, in five filterable values: Open source, Mixed, Source available, Proprietary, Unverified |
| `oss_detail` | The precise wording behind that status, naming whether the restriction falls on code, model weights, a dataset, or service terms |
| `price_class` | The price of the project's **own software**, separately from any hosted subscription sold alongside it |
| `software_price_note` | Verified amounts, with currency, billing period, seat counts, credit allowances and threshold conditions preserved as recorded |
| `cost_flags` | Conditions that are not the software fee: mandatory paid dependency, optional paid hosting, dedicated hardware, self-hosting infrastructure, staff effort, or none material |

Four rules govern how these are filled in.

**Code, model, dataset and service terms stay distinct.** A dataset is classified as carrying an
open or restricted *data licence*, never as "open-source software". A project whose code is MIT
but whose weights or reference data carry non-commercial terms is `Mixed`, with `oss_detail`
naming which part is restricted. Where the restriction comes from data the project *consumes*
rather than ships, that is stated too.

**Unresolved stays unresolved.** Where no licence file, SPDX identifier or licence statement
could be confirmed, `licence_type` is `Unresolved` and `oss_status` is `Unverified`. These are
not quietly rounded to permissive. A separate flag, `licence_spdx_verified`, records whether the
licence file itself was read, as distinct from the licence being named by the GitHub API or the
project's documentation — the second is a research note, not a verified determination. Both
counts are published in
[Findings](findings-and-limitations.md#licensing-and-pricing-that-remain-unverified).

**The software fee is separated from the subscription.** `price_class` describes what it costs
to obtain and run the software, read from the project's own price statement. An optional hosted
tier sold by the same vendor is recorded in `cost_flags` and priced in the note, not folded into
the project's price. A dependency's free tier is never reported as the project's free tier.

**A mandatory paid dependency is stated first.** Where a paid API, dataset, model, licence or
tool is required for the core function, it is flagged and shown in bold ahead of every other
cost, because it determines whether the project is usable at all rather than what it costs.
Optional paid extras are labelled as optional. Infrastructure you operate is separated from
charges a vendor levies, and infrastructure figures are labelled as estimates with the
assumption stated.

Where the records do not establish a price, the field reads **Unknown / not verified**. That is
a statement about the evidence, not a finding that the project is free. Prices were read from
vendor pages on the verification dates recorded against each project and change without notice.

The derived fields are written into the records by `work/enrich_records.py`, which classifies
from the hand-written licence and cost prose and then applies the hand-reviewed corrections in
`work/enrich_overrides.json`. Each correction records its reason. They are stored in the records
rather than computed during the build so that they are visible, diffable and reviewable in
version control, and so that `build.py` validates them like any other field.

## Reproducibility

The canonical data is [`records/`](../records/) — 43 hand-authored JSON files containing one
object per project. Everything else is generated:

```
python3 build.py
```

This reads `records/*.json` plus the narrative fragments in `narrative/` and writes
`catalogue.json`, `catalogue.csv`, `report.md`, `README.md` and the pages under `docs/`.
It validates every record against a required-field list, checks verdict and maintenance values
against controlled vocabularies, rejects out-of-range scores and detects duplicate IDs. The
build prints a validation-error count; the committed state has **zero errors**.

Project IDs (`JAI-A2-35`, `SUR-B3-01`, `OSINT-C1-29`) are stable and are the primary key across
the records, all three exports, the per-project pages and the cross-references between
assessments.

## Known limits of this method

- Nothing was installed or run, so capability scores are documentary judgements.
- Documented user feedback is thin. Where no user reports were found, the assessment says so
  rather than inferring consensus from popularity.
- Hosted services cannot be assessed for maintenance the way repositories can; those entries are
  deliberately marked `Uncertain` rather than assumed to be continuous.
- Model weights were not individually verified for every project that downloads them; where the
  code licence is clear and the weights licence is not, the assessment states that explicitly.
- The ranking encodes one organisation's priorities. It is not a general quality ordering.
