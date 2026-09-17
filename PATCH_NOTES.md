# Paper Reader v0.5 Patch

This patch is designed to overlay your existing `paper-reader-skill` repository.

## Adds

```text
skills/paper-reader/capabilities/paper-compare.md
skills/paper-reader/references/collection-protocol.md
```

## Replaces

```text
skills/paper-reader/SKILL.md
skills/paper-reader/references/paper-context.md
skills/paper-reader/capabilities/paper-note.md
README.md
README_zh.md
WORKFLOW.md
docs/architecture.md
tests/scenarios.md
tests/validate_skills.py
CHANGELOG.md
```

Existing structure/teacher/evidence/context-research/critic/figure-handling files remain unchanged.

## Apply

From the extracted patch directory:

```bash
chmod +x apply-v0.5.sh
./apply-v0.5.sh /path/to/paper-reader-skill
```

The script copies `overlay/` into the target repository and runs:

```bash
python3 tests/validate_skills.py
git diff --check
```

## Main behavior changes

### Continuous notes

```text
context_revision
note_sync: auto | on-demand | off
```

Existing Notes are incrementally merged/revised rather than replaced.

### Collections

```text
.paper-reader/collections/<collection-id>/
├── manifest.md
├── comparison.md
└── synthesis.md
```

### Compare

```text
/paper-reader compare ...
```

The compare flow reuses individual Paper Contexts and backfills only missing comparison fields.

## Important

The validator is meant to run **after the overlay is applied to the full repository**.
