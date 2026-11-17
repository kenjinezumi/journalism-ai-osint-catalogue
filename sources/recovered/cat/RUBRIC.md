# Scoring rubric — MUST be applied identically by every assessor
Research/verification date: 2026-11-16. Context: senior software/AI engineer supporting
independent journalism and media organisations, INCLUDING MEDIA IN EXILE (so hostile-state
threat models, source protection and local/self-hosted processing carry real weight).

Weights: relevance 30 | capability 20 | maintenance 15 | privacy 15 | usability 10 | licence_cost 10
Weighted total = sum(score_i/5 * weight_i), rounded to a whole number out of 100.

## 1. relevance_journalism (30%) — fit to journalism / OSINT / source-protection workflows
0 = no plausible journalistic use; generic infrastructure
1 = conceivable use but far from any reporting workflow
2 = useful in a general data/IT sense; journalism use is incidental
3 = clear supporting role in a reporting or investigation workflow
4 = directly serves a common investigative task; built for or widely used in this domain
5 = core investigative capability; purpose-built for journalism/human-rights work or
    indispensable to a standard newsroom workflow

## 2. capability (20%) — demonstrated functional capability and practical usefulness
0 = claims only, no working implementation evidenced
1 = toy/demo scope
2 = works for narrow cases; significant functional gaps
3 = solid, does its stated job competently
4 = strong, well-engineered, handles real-world messy input at useful scale
5 = best-in-class for its task with evidence of production use at investigative scale

## 3. maintenance (15%) — maintenance, reliability, operational maturity
0 = archived/discontinued with no successor
1 = dormant; stale dependencies; unpatched risk
2 = declining; sporadic fixes; key deps aging
3 = stable with low activity — mature and still functional (NOT a penalty for a finished tool)
4 = actively maintained with regular substantive releases
5 = actively maintained, versioned releases, responsive issues, security process, institutional backing
NOTE: frequent commits != quality; infrequent commits != abandonment. Judge substantive
activity (functional commits, releases, security fixes) over dependabot/doc noise.

## 4. privacy_deployment_control (15%) — can sensitive material stay under your control
0 = mandatory third-party cloud; sensitive data necessarily leaves your infrastructure
1 = hosted-only with no self-host path, but data exposure limited
2 = self-hostable but core features require external APIs/telemetry by default
3 = self-hostable; some optional external calls that must be configured off
4 = fully self-hostable/local with no required external calls
5 = designed for local/offline/air-gapped use; privacy is the explicit design goal
NOTE: local hosting alone does NOT make a workflow secure — note residual risks.

## 5. usability_integration (10%) — usability, documentation, integration effort
0 = no docs; unusable without reading source
1 = minimal readme; expert-only
2 = usable by an engineer after real effort; thin docs
3 = decent docs; straightforward for an engineer; non-engineers need help
4 = good docs, packaged installs or containers, clean API/CLI
5 = excellent docs and packaging; a non-technical journalist can use it unaided

## 6. licence_cost (10%) — licensing and cost suitability for a commercial/NGO newsroom
0 = licence or cost blocks the intended use (non-commercial weights, prohibitive fees)
1 = severe restrictions or high mandatory cost
2 = usable but with real constraints (strong copyleft on a product, paid data dependency)
3 = permissive-enough code but a notable paid/licensed dependency
4 = OSI licence, no mandatory fees, minor caveats
5 = OSI permissive, no mandatory external costs, clean for commercial publication
NOTE: strong copyleft (AGPL) is NOT automatically a low score — it only matters where the
newsroom intends to redistribute or host a modified network service. Score the actual impact.
NOTE: do NOT assume NGO use satisfies a non-commercial restriction.

## Evidence confidence (stated separately, NOT folded into the score)
high   = primary sources verified (licence file read, API metadata, official pricing page)
medium = official docs/README reviewed; some fields inferred from reliable secondary sources
low    = limited or conflicting evidence; several fields unverified → mark assessment provisional

## Assessment depth (must be stated honestly per project)
docs-reviewed | repo-inspected | metadata-verified | installed-and-tested
NEVER claim installed-and-tested. Nothing in this survey was installed or run.

## Verdicts
Adopt | Pilot | Integrate | Monitor | Reference only | Avoid for new deployment
For Monitor/Reference/Avoid, name a better catalogue alternative where one exists.

## Material blockers (tracked in a SEPARATE field, never silently inside the score)
e.g. "weights CC-BY-NC — unusable for commercial publication", "requires paid satellite
tasking", "platform API withdrawn", "unmaintained security tool", "ethical-source licence".
