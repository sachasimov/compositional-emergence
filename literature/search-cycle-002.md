# Focused methods search/access log — cycle 002

Date: 2026-11-18. Author: Literature Scientist agent. Scope: resolve the two
cycle-001 reading leads, inspect relevant definitions and assumptions, and repair
the Cook PDF route noted by the critic. This is a bounded targeted review, not a
new exhaustive novelty search. The cycle-001 files are unchanged history.

## Search procedure

Used connected `search_service_web_run` with these exact queries in one batch:

1. `Rupe Crutchfield Local causal states discrete coherent structures 2018 075312`
2. `Balduzzi Detecting emergent processes cellular automata excess information 1105.0158`

Results surfaced arXiv, author/institutional originals, publisher routes, and
secondary indexes. Secondary accounts were not used to fill primary-text gaps.
No result count, per-query rank, or exhaustive absence claim is inferred from
the combined response. Direct opens of previously supplied URLs preceded the
queries; explicit section/phrase finds then located the material in the dossier.

## Successful retrievals

- Rupe/Crutchfield: opened arXiv abstract and the 27-page full PDF; then downloaded
  `https://arxiv.org/pdf/1801.00515v1` with Python `urllib.request`. Checked §II B1
  and B2, §III B, and §IV C2/Fig. 10. Version history lists v1 only; printed draft
  date differs from arXiv submission by two days. Final journal text was not
  compared with this draft.
- Balduzzi: opened `https://arxiv.org/html/1105.0158v2` and abstract/version history;
  downloaded `https://arxiv.org/pdf/1105.0158v2`. Checked the named algorithm,
  information, Life and Hopfield sections in the dossier. HTML headings and
  equation numbers are stable locators; no journal version is asserted.
- Cook: audit record suggested
  `https://content.wolfram.com/sites/13/2023/02/15-1-1.pdf`. It opened and downloaded
  successfully (40 pages); §§1–2 and 2.3 were spot-checked, not the entire proof.
  An additional 2018/02 route opened successfully but is not the archived hash
  identity. Do not assume both routes are byte-identical.
- Local PDF checks used `pdftotext -layout`, followed by section/phrase searches;
  formulas were checked in the primary extraction, without relying on OCR line
  breaks for theorem transcription. No formula or theorem was newly implemented.

## Failed or limited retrievals retained

- `https://csc.ucdavis.edu/~cmg/papers/dcs.pdf`: web tool rejected content length
  12,632,787 bytes; use the version-pinned arXiv preprint instead. This amends
  the prior cycle's unresolved reading lead without deleting its earlier timeout.
- `https://escholarship.org/uc/item/20r4d14j`: JavaScript anti-bot response.
- `https://doi.org/10.1063/1.5021130`: inaccessible publisher/CDN redirect.
  Publisher-final proof verification is not claimed.
- Balduzzi institutional record initially readable, later 403 on a follow-up
  viewport request. Primary arXiv full text remained accessible.
- Cook old `https://www.complex-systems.com/pdf/15-1-1.pdf` still returned 404;
  an added `?download=1` route also failed. The new working route does not make
  those historical failures false. No authentication wall was bypassed.

## Reproduction of source identity

[source-artifacts-cycle-002.json](source-artifacts-cycle-002.json) records exact
download URLs, final URLs, dates, lengths and SHA-256 values for the three PDFs.
Retrieve with ordinary HTTPS, check the PDF signature, and hash the returned
bytes using SHA-256; compare against the recorded identity. Publisher/arXiv PDF
regeneration can change bytes, so a hash mismatch requires a version/content
check rather than an assumption that scientific content changed. Public PDFs are
cached outside the repository; the committed manifest is not a copy of a paper.

Check claims against the dossier's exact sections, not search summaries. No
independent numerical replication, detector comparison, author contact, or
further search cycle was performed. Source inspection and literature verification
do not count as original experimental results.
