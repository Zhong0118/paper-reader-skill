# Architecture

`paper-reader` remains one public Agent Skill.

v0.5 has three state layers:

```text
Single Paper State
    ↓
Paper Context
    ↓
Durable Note

Multiple Paper States
    ↓
Collection
    ↓
Comparison + Synthesis
```

## Internal capabilities

1. `paper-structure`
2. `paper-teacher`
3. `paper-evidence-review`
4. `paper-context-research`
5. `paper-method-critic`
6. `paper-compare`
7. `paper-note`

Only `skills/paper-reader/SKILL.md` is public.

## Paper Context as source of truth

A Note is derived from Paper Context.

Substantive changes increment `context_revision`. Notes record `synced_context_revision`.

This supports reliable incremental synchronization without treating “stage has run” as “all knowledge is complete.”

## Incremental Note Sync

```text
Context update
→ stable knowledge node
→ affected managed region
→ merge/revise/deduplicate
→ preserve user content
```

Policies:

```text
auto
on-demand
off
```

Sync does not trigger new analysis.

## Collection layer

A collection never replaces individual Paper Contexts.

```text
Paper A Context ─┐
Paper B Context ─┼─→ Manifest → Comparison → Synthesis
Paper C Context ─┘
```

Large folders are inventoried and triaged before deeper reading.

Comparison axes are normalized across papers. Missing coverage is backfilled only where needed.

## Separation of outputs

Single-paper knowledge:

```text
papers/<paper-id>/context.md
papers/<paper-id>/note.md
```

Cross-paper knowledge:

```text
collections/<collection-id>/manifest.md
collections/<collection-id>/comparison.md
collections/<collection-id>/synthesis.md
```

Collection-wide synthesis is not copied wholesale into individual Notes.

## Evidence semantics

Cross-paper cells distinguish:

```text
reported
derived
not_reported
not_assessed
not_accessible
not_applicable
uncertain
```

This prevents coverage gaps from being mistaken for negative findings.

## Research boundary

`paper-context-research` explores literature around one target paper.

`paper-compare` compares a user-defined paper set.

Neither automatically becomes a general open-ended research agent.
