# Paper Reader Skill

[中文说明](README_zh.md)

A single-entry Agent Skill for **deep paper learning, continuously updated notes, and evidence-backed comparison of defined paper collections**.

Recommended explicit invocation:

```text
/paper-reader <mode>
```

Natural-language routing remains supported.

## 9 user-facing modes

| Mode | Purpose |
|---|---|
| `quick` | Quick single-paper structure |
| `deep` | Deep reading + light context |
| `internal` | Deep reading with no external sources |
| `teach` | Explain equations, methods, concepts, mechanisms |
| `context` | SOTA, benchmarks, author prior work, follow-ups, surveys |
| `critique` | Evidence and methodology critique |
| `compare` | Compare multiple supplied papers or a paper folder |
| `note` | compact / learning / full note |
| `full` | Complete single-paper workflow + Full Learning Record |

Examples:

```text
/paper-reader deep
/paper-reader compare Compare these papers by material type, macrophage mechanism, and bone-regeneration outcome
/paper-reader note learning
```

## Continuous Note Sync

Paper Context is the single-paper source of truth. A persisted Note is a derived artifact.

Substantive Context changes increment:

```yaml
context_revision: 7
```

Notes track the revision they contain:

```yaml
synced_context_revision: 7
```

Default:

```yaml
note_sync: auto
```

Supported policies:

- `auto` — incrementally merge substantive new/revised knowledge into existing Notes;
- `on-demand` — sync only when the user explicitly asks to save/update a Note;
- `off` — never modify an existing Note automatically.

Sync is a persistence operation, **not a trigger for new reading or new web research**.

Managed model regions may use:

```html
<!-- paper-reader:managed:start key="teaching.T1" -->
...
<!-- paper-reader:managed:end -->
```

User content may use:

```html
<!-- paper-reader:user:start -->
...
<!-- paper-reader:user:end -->
```

User-authored content is preserved. Existing Notes are section-merged and deduplicated rather than wholesale replaced.

## Multi-paper collections

Each paper keeps an independent Paper Context / Note.

A collection adds:

```text
.paper-reader/collections/<collection-id>/
├── manifest.md
├── comparison.md
└── synthesis.md
```

For large folders the default flow is:

```text
inventory
→ metadata / abstract triage
→ choose comparison axes
→ reuse existing Paper Contexts
→ backfill only missing comparison fields
→ normalized matrix
→ synthesis
```

It does **not** default to `full × N`.

## Real comparison, not parallel summaries

`compare` first normalizes papers onto the same axes.

A comparison cell distinguishes:

```text
reported
derived
not_reported
not_assessed
not_accessible
not_applicable
uncertain
```

This prevents “not read yet” from being misreported as “the paper does not contain it.”

Key comparison claims retain paper + section/figure/table/source provenance.

## Note vs Collection outputs

Single-paper Note remains about that paper.

Collection-wide results go to:

```text
comparison.md
synthesis.md
```

A single-paper Note may link to those files, but does not absorb the entire multi-paper comparison.

## Internal capabilities

Only `paper-reader` is public. Internally it orchestrates seven capabilities:

```text
paper-structure
paper-teacher
paper-evidence-review
paper-context-research
paper-method-critic
paper-compare
paper-note
```

## Installation

```bash
npx skills add https://github.com/Zhong0118/paper-reader-skill --skill paper-reader
```

or:

```bash
git clone https://github.com/Zhong0118/paper-reader-skill.git
cd paper-reader-skill
./install.sh ~/.agents/skills
```

## Validation

```bash
python3 tests/validate_skills.py
git diff --check
```

See `WORKFLOW.md` and `docs/architecture.md` for the full protocol.
