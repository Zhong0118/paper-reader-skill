# Architecture

`paper-reader` is a single public Agent Skill that orchestrates six private capabilities around one shared Paper Context:

1. `paper-structure`
2. `paper-teacher`
3. `paper-evidence-review`
4. `paper-context-research`
5. `paper-method-critic`
6. `paper-note`

The only public skill is `skills/paper-reader/SKILL.md`.

## Invocation layer

The user-facing invocation layer is intentionally separate from the internal routing layer.

Recommended explicit semantic form:

```text
/paper-reader <mode> <request>
```

User-facing modes:

```text
quick
deep
internal
teach
context
critique
note
full
```

`note` has `compact / learning / full` submodes.

Internal mappings preserve the existing implementation:

```text
internal      → deep-internal
note compact  → archive-compact behavior
note learning → archive-learning behavior
note full     → full-format note from current verified Context
full          → complete six-stage workflow
```

The slash form is a portable explicit-invocation convention for hosts that expose installed Skills this way. The repository does not vendor host-specific command adapters. Natural-language routing remains available.

## Source separation

The shared context separates `paper_internal` from `external_context`. External claims retain provenance and retrieval date. Later work cannot silently rewrite what the target paper originally claimed.

## Search scope

Context research is paper-centered, not an open-ended literature review.

Research types:

```text
none / light / targeted / full
```

Deep reading defaults to light context. Targeted questions may go deeper on one issue than full research. Search remains question-driven without source quotas.

## Coverage and persistence

Reading depth and archival output are independent.

Notes use:

```text
compact / learning / full
```

`note full` means full-format rendering of the current verified Context; it does not imply that missing stages were completed. `full` means the complete reading workflow plus the full-format note.

Stage status is scoped to material actually read and tied to paper version. Source changes invalidate affected dependent assessments while preserving unrelated findings and user annotations.

## Shared figures

`references/figure-handling.md` is used by stages that explain, assess, or archive figures. Visual verification and saving remain separate. Original figures and model redraws remain distinct.
