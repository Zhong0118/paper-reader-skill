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

## Coverage and persistence

Reading depth and archival output are independent. Compact archive saves existing results and gaps; learning archive organizes standard study notes and supplements useful light context; full explicitly fills necessary analysis. Stage status is scoped to material actually read, tied to the paper version, and supports partial or blocked work. Legacy completed_stages is only a hint. Source changes invalidate affected dependent assessments and notes while preserving unrelated findings and user annotations.

Notes have compact, learning and full formats. Deep reading defaults to light research; explicit paper-only reading suppresses external context. Research types none/light/targeted/full describe scope rather than a strict ranking. Targeted questions can deepen existing full coverage. Stored depths reflect actual work, with partial/blocked states tracked separately. Search remains question-driven without source quotas; stable findings are reused and current claims refreshed.

## Shared figures

`references/figure-handling.md` is loaded by stages that explain, assess or archive figures. It separates visual verification from saving, tracks caption-only access, and requires source/version/page/caption/claim linkage for selected assets. Original figures and model redraws remain distinct. This is a shared reference, not a seventh stage.
