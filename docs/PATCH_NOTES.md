# v0.4.1 Slash Invocation Update

Replace these files in your current repository:

```text
README.md
README_zh.md
CHANGELOG.md
WORKFLOW.md
docs/architecture.md
skills/paper-reader/SKILL.md
tests/scenarios.md
tests/validate_skills.py
```

No changes are required to the six capability files or Paper Context / Figure Handling references.

## User-facing invocation

Recommended:

```text
/paper-reader <mode> <request>
```

Main modes:

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

Note submodes:

```text
compact
learning
full
```

Important:

```text
/paper-reader note full
```

means “render a Full Learning Record from current verified Context.”

```text
/paper-reader full
```

means “perform the complete six-stage workflow, then render a Full Learning Record.”

## Apply

Copy the files over the matching paths in your repository, then run:

```bash
python3 tests/validate_skills.py
git diff --check
```

The update does not add host-specific command adapters. `/paper-reader` is the recommended explicit invocation convention for hosts that expose installed Agent Skills this way; natural-language routing remains the portable fallback.
