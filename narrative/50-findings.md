## Significant findings

### Licensing — the ones that will actually bite

1. **MVT and androidqf are not OSI-licensed.** MVT License 1.1 §3.0 requires the Data Owner's
   explicit, uncoerced, fully informed consent *including disclosure of your data-retention and
   disposal policy*. Quoted verbatim in `sources/evidence/leads.md`. Build the consent script.
2. **SuperGlue is academic/non-profit noncommercial only** (Magic Leap agreement, read this
   session). It is the most-cited matcher in geolocation pipelines, GitHub reports NOASSERTION so
   scanners miss it, and hloc's default pipelines can pull its weights. Use LoFTR (Apache-2.0).
3. **Marker and Surya weights are OpenRAIL-M** with a commercial threshold of **$5M revenue OR
   funding** ($2M for Chandra) — verified on datalab.to/pricing. Docling is the licence-clean
   alternative.
4. **Do No Harm licence** on Forensic Architecture's timemap and mtriage: clause 4 bars use by
   organisations deriving majority income from a listed set of activities, and clause 5 makes it
   viral on redistribution. Both repositories are also dormant.
5. **OpenSanctions: code MIT, data CC-BY-NC-4.0.** The data is the restricted layer and
   commercial use needs a paid licence (quote only). "OpenSanctions is open source" is true of
   the code only.
6. **Tracker Radar is CC-BY-NC-SA-4.0 data**, not software — NonCommercial plus ShareAlike, and
   GitHub reports NOASSERTION.
7. **CC-BY-NC on model weights** where you would not expect it: GLiNER v0/v1 checkpoints (the
   ones most tutorials link to), NVIDIA Sortformer diarisation, DeepfakeBench. The Apache-2.0
   code licence never cures a restricted weights licence.
8. **Non-OSI "open" tools:** n8n is Sustainable Use Licence (fair-code); MinerU is Apache-2.0
   *plus unread restrictive additional terms*; TruFor, Noiseprint, SBI and LAA-Net are all
   academic or non-profit-only.
9. **OnionShare is GPL-3.0** — session 1's error came from reading a bundled third-party licence.
   Corrected with primary evidence.
10. **AGPL network copyleft** matters in exactly one place people miss: embedding wabac.js in a
    public newsroom web application. Take advice before shipping that.

### Maintenance — what died, and why

Of 361 projects: 228 actively maintained, 72 stable with low activity, 18 declining, 25 dormant,
6 archived, 12 uncertain.

**Archived (confirmed `archived=true`):** Telethon (MIT, 12k stars — Telegram collection
pipelines inherit the risk) · Kùzu (embedded graph DB, final release 2025-10-10) ·
news-please (still widely recommended in data-journalism material) · pagodo · Whoogle ·
CooRnet · meedan/fetch.

**The pattern:** almost everything that died in 2024-2026 died because a **platform API or
scraping path was withdrawn**, not because maintainers lost interest. CrowdTangle killed CooRnet;
Google's anti-scraping killed Whoogle and automated dorking. Design collection layers so the data
source is replaceable without rewriting the analysis — CooRTweet versus CooRnet is the model.

**Declining but undeprecated, which is the dangerous state:** alephdata/aleph (use OpenAleph) ·
alephdata/followthemoney 3.x (use opensanctions/followthemoney 4.x — the old URL does *not*
redirect) · dedupe (no push since 2025-07-29; use Splink) · olmOCR (no activity since March 2026)
· Klaxon self-hosted (README warns it may miss changes) · Hyphe · Overview · Atlos (no release in
14 months, holding investigation-critical data).

**22 repository transfers verified by redirect**, including faster-whisper → SYSTRAN,
marker/surya → datalab-to, sentence-transformers → huggingface, DVC → **treeverse**,
Presidio → data-privacy-stack, NVIDIA/NeMo → NVIDIA-NeMo/Speech, Ragas → vibrantlabsai.
Pinned git URLs keep working; SBOMs and provenance records should be updated.

**17 session-1 candidate paths were genuine 404s** — bad discovery guesses, each resolved to its
real home in `sources/evidence/leads.md`.

### Pricing — verified, and deliberately unpriced

Verified from vendor pages with currency, period and basis: Transkribus (EUR0-449/yr plus credits)
· Datalab ($5M threshold; hosted Free/$400/mo Team) · Maltego (EUR3,000-7,500/yr per seat) ·
pyannote.ai (EUR0.035-0.198 per audio-hour) · Neo4j (Community free GPL-3; AuraDB from
$0.09/GB/hour; Enterprise quote-only) · Gemini API per-million-token rates with dated increases.

**Sentinel Hub / Planet: not publicly listed — quote required.** Re-verified twice: the
sentinel-hub pricing page returns only a redirect to planet.com/pricing, which renders no prices.
Treat commercial satellite imagery as an unpriced dependency and build on openly licensed
Sentinel/Landsat via pystac wherever the story allows.

**Have I Been Pwned figures are LOW confidence** — from secondary sources, not verified on the
vendor page. Do not budget against them.

**Deliberately not asserted:** DocumentCloud, Browsertrix hosted, Perma.cc, MuckRock, Shodan,
Censys, FOFA, Hunter, ZoomEye, Serper, OpenAI, Google Programmable Search, Carrot Search Lingo3G,
Artifex's PyMuPDF commercial licence, OpenCellID, Global Fishing Watch. Each is recorded as
unknown rather than estimated.

### Dependency and operational-security findings

- **Tools that upload by default and are easy to use anyway:** InVID-WeVerify plugin (media to
  AFP/vera.ai plus Google/Baidu/Yandex) · `datasette publish` · Perma.cc link creation ·
  ArchiveBot requests (public IRC) · OpenRefine reconciliation · Marker's LLM-enhancement mode ·
  Surya's configurable remote inference endpoint · webchanges' AI summaries · kuroi against a
  hosted model. Each is one click or one config line from disclosing an investigation.
- **Queries that disclose your targets to commercial vendors:** uncover and Mihari (scan
  databases) · streetlevel (Google/Apple/**Yandex**) · Maltego transforms · OpenCellID API.
- **The worst irony in the catalogue:** kuroi exists to find and remove source-identifying data
  and, pointed at a hosted LLM, transmits the unredacted documents to that provider.
- **Three tools whose own presence endangers the user** in a hostile jurisdiction: Tails (the
  USB), Orbot (the app), Tella (the camouflaged app). Brief people honestly.
- **Two dependency traps worth naming:** `alephdata/followthemoney` is two major versions behind
  with no redirect; grab-site depends on wpull, dormant since April 2024, so both layers stalled.
