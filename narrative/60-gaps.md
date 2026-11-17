## Remaining evidence gaps and provisional conclusions

23 projects are marked **provisional** and 13 are **low confidence**. The substantive gaps:

1. **Unresolved licences** (treat reuse as legally unclear): AVeriTeC, ClaimsKG extractor,
   ASVspoof 2021 baselines, Deepfake-Eval-2024, dorks_hunter, stalkerware-indicators,
   AmnestyTech/investigations. Indicator repositories without licences are a systemic problem.
2. **MinerU's additional terms were recorded as restrictive in session 1 but not characterised.**
   Get a legal reading before any commercial use.
3. **Stanza's model archives have no stated licence** while the code is Apache-2.0. Unresolved
   commercial-use risk for derived published datasets.
4. **Hosted-service maintenance cannot be evidenced like a repository's.** Google Fact Check
   Tools API, Internet Society Pulse, DataIndex.us, Microsoft Planetary Computer, OpenCellID and
   the Senate LDA database are classified Uncertain on purpose, not by omission.
5. **Bot protection is not evidence of removal.** OpenSecrets and lda.senate.gov returned 403 to
   `curl`; both are recorded as live-but-unverified. The **EU Transparency Register** is the one
   genuinely unresolved source URL — the old ec.europa.eu path 404s.
6. **Scoop's cryptographic signing format was not independently verified** beyond the
   maintainers' description. Confirm with Harvard LIL before relying on it in a legal filing.
7. **Model weights not individually verified** for Docling, PaddleOCR, Alegre's bundled
   checkpoints, RAGFlow's parsing models, Kraken's Zenodo models and several spaCy and Stanza
   language packs. In each case the code licence is clear and the weights are not.
8. **No project was installed or run.** Every capability claim rests on documentation, repository
   inspection and API metadata. The three I would want hands-on before committing budget are
   OpenAleph (Elasticsearch sizing), RAGFlow (whether reporters trust it appropriately) and
   Rayhunter (false-positive rate on your actual networks).
9. **Feedback is thin by design.** Where I found no documented user reports, the card says so.
   Issue-to-star ratios and release cadence are used as *maintenance* evidence, never as proxies
   for quality or for user satisfaction.
