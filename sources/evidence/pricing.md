# Pricing evidence

## Inherited from session 1 (verification_date 2026-11-16, read from vendor pages)
The full line-item table is preserved verbatim at `../recovered/cat/pricing.tsv` (23 rows).
Summary of what was verified there, with the confidence session 1 assigned:

| vendor / layer | verified figure | confidence |
|---|---|---|
| OpenSanctions data licence | data CC-BY-NC 4.0; commercial use requires a paid licence; Screening API sold as prepaid credit bundles with free credits on signup; Screening Licence and Reseller/OEM **quote-only** | high (official) |
| Transkribus | Free EUR0/yr (50 credits/month, 1 seat, 20GB); Scholar EUR99/yr or EUR19.99/mo (900 credits/yr, 1 seat, 200GB); Team EUR449/yr or EUR69/mo (1,500 credits/yr, 5 seats, 1TB); Organisation quote (75,000+ credits/yr, 15+ seats). Credits: HTR 1/page, line detection 0.25/page, table recognition 1/page, field recognition 1/page; on-demand 250 credits = EUR59.50, never expire | high (official) |
| Datalab (Marker/Surya/Chandra weights) | free for commercial use below BOTH revenue and funding thresholds: **$2M for Chandra, $5M for Marker and Surya**; above either, a commercial licence is required | high (official) |
| Datalab hosted API | Free $0 pay-as-you-go with $20 (work email) / $10 (personal email) monthly allowance; Team $400/month; Enterprise custom | high (official) |
| Maltego | Basic free forever (200 credits/mo) or Basic+ (1,000 credits/mo), Community Edition graph only; Entry EUR3,000/yr (10,000 credits/mo, includes Hunchly); Professional EUR7,500/yr (20,000-40,000 credits/mo, up to 5 users, per seat); Enterprise quote (5+ users) | high (official) |
| pyannote.ai hosted | Diarization Precision-3 batch EUR0.112/hour of audio; Community-1 batch EUR0.035/h; Live-1 streaming EUR0.198/h. Developer EUR19/mo and Starter EUR99/mo (each including matching credit); Enterprise custom. Free trial 150 hours identification + 10 voiceprints for one month | high (official) |
| Neo4j | Community Edition GPL-3, free download. Enterprise and Infinigraph: **quote required**. AuraDB Free $0; Professional from $0.09/GB/hour (min 1GB); Business Critical from $0.20/GB/hour (min 2GB); Virtual Dedicated Cloud quote. Hourly metering includes storage, compute, IO, network, backups | high (official) |
| Have I Been Pwned | Pwned Passwords API free, no rate limit, no subscription. Breach/domain search tiers reported as Pwned 1 ~$3.95/mo (25 breached addresses, 10 req/min) and Pwned 2 ~$16.95/mo (100 addresses, 50 req/min); annual = pay 10 get 12 | **LOW** — official page not machine-readable; figures from secondary sources, NOT verified on the vendor page |
| Google Gemini API | Gemini 4 Carbon in $2.00/M tokens to 2026-11-30 then $4.00; out $10.00/M then $20.00; no free tier for Carbon. Gemini 4 Hydrogen in $1.50/M, out $7.50/M, free tier available. Gemini 3.8 Flash in $0.75/M to 2026-12-31 then $1.50; out $3.75/M then $7.50. Gemini 3.5 Flash-Lite in $0.30/M, out $2.50/M; Gemini 3.1 Flash-Lite in $0.25/M (text/image/video) or $0.50/M (audio), out $1.50/M | high (official) |

## Re-verified or newly verified in this session (2026-11-17)

### Sentinel Hub / Planet — CONFIRMED not publicly listed
Session 1 recorded Sentinel Hub pricing as unverified because the pages redirect to Planet.
Re-checked this session and the finding stands:
- `https://www.sentinel-hub.com/pricing/` returns only a redirect notice pointing to
  `https://www.planet.com/pricing/` — no tiers, currency, period or processing-unit limits.
- `https://www.planet.com/pricing/` renders a "Planet Pricing" header with **no prices,
  tier names, quotas or currency** retrievable.
**Record as: not publicly listed — quote required.** Sentinel Hub is part of Planet; any
satellite-imagery budget line must come from a vendor quote, not from this catalogue.
Consequence for planning: the free and research tiers that Sentinel Hub historically offered
cannot be confirmed as still available, so treat commercial satellite access as an unpriced
dependency and prefer openly licensed Sentinel/Landsat data where the story allows.
Verified 2026-11-17, confidence high for "not publicly listed", no confidence in any figure.

### Prices deliberately NOT asserted in this catalogue
The following appear in project entries as costs that exist but were **not verified** here, and
are recorded as unknown rather than estimated: DocumentCloud organisational tiers; Browsertrix
hosted plans; Perma.cc institutional tiers; MuckRock/DocumentCloud account tiers; Shodan,
Censys, FOFA, Hunter and ZoomEye API tiers (required by `uncover`); Serper and OpenAI API rates
(required by Loki/FacTool/DEFAME); Google Programmable Search quota pricing (required by
AVeriTeC); Google Fact Check Tools API quota terms; Carrot Search Lingo3G; Artifex's commercial
PyMuPDF licence; commercial licences for MVT-restricted, GRIP-UNINA, SnT and Magic Leap
academic-licensed components (no public commercial path published for several of these).

**Rule applied throughout:** vendor prices are quoted verbatim with currency, period and basis.
Infrastructure figures are my own estimates, always labelled as estimates with assumptions
stated. "No software licence fee" is never reported as "free" where infrastructure or staff
effort is material.
