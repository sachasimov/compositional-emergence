# Focused source and access log — cycle 003

Date: 2026-11-18. Author: Literature Scientist agent. Base:
`aeed31d4487908029b0107f253f8329a795a78cd`. Scope: re-inspect existing primary
references for phase recognition, segmentation/identity, interaction and
nonunique granularity. No broad resurvey or absence-of-prior-art claim.

## Bounded search and retrieval

Connected `search_service_web_run` queries, exact strings in one batch:

1. `Hanson Crutchfield ECA54 particle phases collisions 1997 filter`
2. `Shalizi coherent structure filters sensitivity statistical complexity 2006 distinction`

Primary URLs were opened directly in the same call. Results were combined; no
per-query rank, exhaustive count or novelty inference is made. Existing checked
references supplied the relevant evidence, so no additional substantive source
was added. Secondary explanations were not substituted for primary text.

Retrieved and locally cached outside the repository:

| ID | Version and exact URL | Targeted inspection |
|---|---|---|
| HC1997 | Author-hosted published PDF, `https://csc.ucdavis.edu/~cmg/papers/ECA54.pdf` | §4.2 synchronization/filtering; §5.1 phases, all-phase strings and subparticles; §5.2 collision shifts/Table 1. |
| S2006 | `https://arxiv.org/pdf/nlin/0508001v1` | §II A perturbation construction; §III predictive states; §IV C complementary filtered descriptions. |
| RC2018 | `https://arxiv.org/pdf/1801.00515v1` | §II B1 prediction/direct-cause distinction; §III B structure semantics; §IV C2/Figs. 9–10 representation and finite-horizon artifacts. |

Web extraction was cross-checked against local `pdftotext -layout` section
searches. No formula was certified from OCR, and no algorithm or source
experiment was reproduced. HC1997 is a published article snapshot; the other two
are pinned preprints, not asserted byte-identical to their journal versions.
The exact claim locators are in [the memo](identity-cycle-003.md).

## Artifact identity and access limitations

All three primary PDF retrievals succeeded in this cycle. The
[manifest](source-artifacts-cycle-003.json) records URLs, versions, final URLs,
content type, byte lengths and SHA-256 hashes from Python `urllib.request`
downloads on the access date. RC2018 matches its cycle-002 byte identity; no
unverified identity is assumed for the newly hashed articles. Historical failures
and checks in prior cycle logs remain unchanged.

To recheck, retrieve the recorded URLs, verify the PDF signature, hash the bytes,
and inspect the named sections. Regenerated PDFs can change hashes; investigate
the version/content instead of assuming the scientific claims changed. No paper
replicas are committed. No publisher-final S2006/RC2018 text or new theorem was
audited; no authors were contacted. The memo's benchmark contracts and conceptual
counterexamples are explicitly our reasoning, not results attributed to these
papers.

The coordinator's cycle-003 scope document was absent at worktree creation and
was read from the coordinating worktree once available. Earlier governance
stop gates are historical; the user's new bounded-cycle authorization controls
this work. Cycle-003 simulation code, new labels, settings and outcomes were not
inspected, and this log records no numerical experiment. Independent audit and
PR handoff end the contribution; no next cycle is initiated.
