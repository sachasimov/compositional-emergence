# Search and access log — cycle 001

Date: 2026-11-18. Interface: connected web search (`search_service_web_run`), then
explicit primary URL opens. Queries below are exact. Rankings and coverage change;
this reproduces a procedure, not an immutable or exhaustive corpus. Only checked
ledger material supports factual assessments; snippets do not verify theorems.

| Batch | Exact query | Relevant outcome |
|---|---|---|
| 1 | `Rosas symmetry common origin hierarchical emergence abstraction aeh0773 2026` | DOI, institutional accepted record, preprint predecessor. |
| 1 | `Rosas Software natural world computational hierarchical emergence 2402.09090` | arXiv v2. |
| 1 | `Israeli Goldenfeld 2006 Coarse graining cellular automata 026203` | APS, author preprint. |
| 1 | `Hanson Crutchfield 1997 computational mechanics cellular automata particles collisions domain` | Author-hosted published PDF. |
| 2 | `Shalizi Haslinger Rouquier Klinkner Moore automatic filters coherent structures cellular automata 2006 local causal states` | APS, arXiv. |
| 2 | `Cook Universality elementary cellular automata 2004 complex systems rule 110` | Publisher abstract, author record. |
| 2 | `Crutchfield calculi emergence 1994 Physica D 75 11 54` | Publisher, author manuscript. |
| 3 | `cellular automata compositional robustness predictive autonomy coupling productivity lifetime encounter rate` | Related forecasting/robustness; no verified exact H2 comparison. |
| 3 | `cellular automata spontaneous multigeneration composition particle collision ancestry` | Hintze/Bohm Outlier: direct prior-art objection. |
| 3 | `Local causal states discrete coherent structures Rupe Crutchfield 2018` | 2018 overlap lead; full text timed out. |

Each batch returned a combined result set; per-query ranks/counts were not
recorded or inferred. No systematic citation graph or exhaustive database search
was completed. Balduzzi `1105.0158v2` was suggested by the independent critic after
the initial searches; it remains an unchecked lead rather than an extra claimed
verification.

## Retrieval failures and decisions

- Read S2 arXiv HTML v2, S3 preprint PDF v1 and APS abstract, S4 published author
  PDF, S5 preprint PDF v1, and S6 author manuscript at the ledger's named sections.
  No numerical reproduction was attempted.
- S1 publisher DOI returned 403. Institutional abstract was readable, its PDF
  redirected to request-a-copy. No request was sent. arXiv `2512.00984v2` returned
  404; v1 was readable. DOI metadata was read through Python `urllib.request`
  from the Crossref works endpoint linked in S1; title/issue/date agreed with the
  inherited citation. Failures are not evidence the paper does not exist.
- S7 `https://www.complex-systems.com/pdf/15-1-1.pdf` returned 404 despite appearing
  in search. Publisher abstract and author record were readable; proof unchecked.
- S8 journal route redirected to inaccessible publisher authentication; arXiv v1
  was readable. Claims use that version.
- `https://csc.ucdavis.edu/~cmg/papers/dcs.pdf` timed out. Rupe/Crutchfield remains
  an uncompleted direct-prior-art lead.

## Recheck procedure

1. Run the exact queries with date and returned URLs; do not assume identical ranks.
2. Open version-pinned ledger URLs and locate named sections/figures. Verify claims
   there rather than from snippets.
3. Cross-check DOI metadata against publisher/author records; distinguish
   publication, acceptance, and preprint revision dates.
4. Preserve contradictory evidence and changed access as amendments. Never silently
   label an unchecked final-version proof verified.

Further search is a proposed next cycle and awaits human approval.
