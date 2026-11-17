# B2 public-records and reference sources — URL verification, 2026-11-17

Session 1 left two lists of candidate source URLs (`../recovered/urls.txt`, `../recovered/u2.txt`)
with no verification. Every URL was checked this session with `curl -L` (and, where a bot-block
was suspected, again with a browser user agent). Results:

| URL from session 1 | status 2026-11-17 | action |
|---|---|---|
| https://ted.europa.eu/en/simple-search | **404** | corrected to https://ted.europa.eu/en/ (200) |
| https://www.usaspending.gov/download_center/custom_award_data | 200 | keep |
| https://sam.gov/ | 200 | keep |
| https://www.opensecrets.org/federal-lobbying | 403 to curl | **not evidence of removal** — bot protection; treat as live, verify in a browser |
| https://lda.senate.gov/system/public/ | 403 to curl | same: bot protection, treat as live |
| https://standards.open-contracting.org/ | no response to curl | corrected to https://www.open-contracting.org/data-standard/ (200) |
| https://docs.opencellid.org/ | 200 | keep |
| https://www.sipri.org/databases/national-reports | 200 | keep |
| https://www.wassenaar.org/control-lists/ | 200 | keep |
| https://www.transparencyregister.europa.eu/ | no response; the older ec.europa.eu path is **404** | **unresolved** — the EU Transparency Register has moved; locate the current entry point before citing |
| https://citizenlab.ca/publication-directory/ | 200 | keep |
| https://privacyinternational.org/ | 200 | keep |
| https://explorer.ooni.org/ , https://api.ooni.io/ , https://data.censoredplanet.org/ | covered by the B1 project entries | keep |
| https://exodus-privacy.eu.org/en/page/trackers/ | **404** | corrected to https://exodus-privacy.eu.org/en/ (200) |
| https://www.stopspying.org/latest-research | **404** | corrected to https://www.stopspying.org/ (200) |
| https://data.europa.eu/data/datasets?locale=en | 200 | keep |
| https://stopstalkerware.org/ , https://www.accessnow.org/ , https://forbiddenstories.org/case/the-pegasus-project/ , https://www.amnesty.org/en/latest/research/2023/10/the-predator-files-caught-in-the-net/ , https://securitylab.amnesty.org/ | reference reading, not catalogued as projects | keep as background |
| https://www.issworldtraining.com/ , https://www.recordedfuture.com/research , https://www.lookout.com/threat-intelligence/research , https://blog.google/threat-analysis-group/ | vendor/industry sources, not open-source projects | keep as background; vendor research is a source, not a tool |
| https://github.com/EFForg/rayhunter/blob/main/LICENSE | verified: GPL-3.0 | catalogued as SUR-B3-13 |

**Method note.** A 403 or an empty response to `curl` is evidence about a bot filter, not about
whether a resource exists. Only the four genuine 404s above were treated as broken, and three of
them had an obvious current equivalent. The EU Transparency Register is the one genuinely
unresolved item and is flagged as an evidence gap rather than quietly dropped.
