# Scientific cycle reporting

Added 2026-11-19 after the user identified that cycle handoffs provided PRs and
test counts without enough explanation of the actual research findings.

Every cycle ends with a scientific status report delivered directly in chat
and saved with the cycle's evidence. The chat version must be self-contained;
opening a PR or reading an earlier progress update must not be necessary to
understand the result. Scale detail to the work, but never omit the finding or
its implication for the central research question.

## Required content

1. **Research status first:** what changed in our understanding, where we are
   against `RESEARCH.md`, and whether this was infrastructure, method validation,
   a hypothesis test, a replication, or an original finding. If the central
   hypothesis was not tested or no novel result established, say so explicitly.
2. **Question and evidence:** the cycle's falsifiable question, what was actually
   run or read, the sampling unit, and the relevant controls and comparisons.
3. **Findings and meaning:** concrete positive and negative observations, what
   they support under the tested conditions, and why that matters. Distinguish
   source results, our observations, and our interpretations.
4. **Numbers with context:** exact counts and denominators, false positives and
   misses, abstentions and unknown labels. Compare methods on identical inputs.
   Do not present different panels as a performance trajectory or authored
   transformations as independent samples. A passed acceptance flag is not
   perfect full-panel performance.
5. **Limits and review:** what the results do not establish, open objections,
   source/access limits, and what the independent reviewer actually checked.
   Re-running the same implementation is not an independent implementation or
   confirmation of the central hypothesis. Tests and PRs belong here as support.
6. **Recommendation and decision:** the specific next question or action, why it
   follows from the evidence, and the remaining decision for the human. List
   proposed merges separately from a proposed new cycle, its scope and budget.
   Report a recommendation to pause or refine definitions when appropriate.
7. **Inspectability:** link the methods report, source ledger, frozen protocol,
   outcomes, review and contribution PRs; keep revision/hash details in the
   evidence appendix when they would obscure the main explanation.

## Completion and approval

The independent critic checks the report's claims against the evidence before
handoff. A cycle is not adequately reported merely because files, review
comments, or PRs were produced. "Tests pass" and "no blockers" are quality
statements, not answers to the research question.

Deliver the report before asking the user to continue. Approval must refer to
the clearly described action and scope; do not infer additional unstated merges
or experiments from a short response. Explicit user instructions take precedence.
Reporting corrections are documentation/review work within the existing cycle,
not authorization to start another experiment or merge its PRs.
