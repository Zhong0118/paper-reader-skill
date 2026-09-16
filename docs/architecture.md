# Architecture

`paper-reader` is a single public Agent Skill that orchestrates six private capabilities around one shared Paper Context:

1. `paper-structure` — extract the paper's research question, argument, method backbone, contributions, experiments and results.
2. `paper-teacher` — teach methods, equations, mechanisms and domain concepts without repeating the summary.
3. `paper-evidence-review` — map each major claim to the paper's own evidence.
4. `paper-context-research` — place the paper in external literature: SOTA, benchmarks, author prior work, predecessors, competitors, follow-ups, surveys, limitations and contradictory findings.
5. `paper-method-critic` — critique methodology using both internal evidence and, when available, external context.
6. `paper-note` — synthesize a durable learning record with related-work comparisons and further-reading paths.

The only public skill is `skills/paper-reader/SKILL.md`. Internal capability files are references loaded on demand, not separately discoverable skills.

## Source separation

The shared context separates `paper_internal` from `external_context`. External claims must retain URL/DOI/title/year/source type and retrieval date when available. A later paper cannot silently rewrite what the target paper originally claimed.

## Search scope

Context research is paper-centered, not an open-ended literature review. It searches only enough to answer where the target paper came from, how it compares, what happened afterward, and what limitations are documented externally.
