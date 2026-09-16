# Paper Reader Skill

[中文说明](README_zh.md)

A single-entry Agent Skill for **deep paper reading, explanation, evidence auditing, literature context, methodology critique, and durable research notes**.

> **Recommended explicit invocation:** `/paper-reader <mode>`. You may also omit the mode, or use natural language if your host has already loaded the skill.

## 30-second start

```text
/paper-reader quick
```
Quick paper structure.

```text
/paper-reader deep
```
Deep reading plus light research context.

```text
/paper-reader internal
```
Deep paper-only reading with no external sources.

```text
/paper-reader teach Explain Equation 4 and Method 3.2
```
Focused teaching.

```text
/paper-reader context Find publication-time SOTA, author prior work, and follow-ups
```
Targeted external context.

```text
/paper-reader critique
```
Evidence and methodology critique.

```text
/paper-reader note learning
```
Standard long-term study / Obsidian note.

```text
/paper-reader full
```
Complete six-stage workflow and Full Learning Record.

## Does `/paper-reader` always work as a native slash command?

`paper-reader` is an **Agent Skill**, not a host-specific command plugin.

- If the host exposes installed Skills through slash or explicit invocation, `/paper-reader ...` is the recommended syntax.
- If the host does not register custom slash commands, select `paper-reader` through that host's Skill UI/mechanism, or use natural language.
- This repository intentionally does not bind itself to Claude Code-, DSH-, or Codex-specific command directories.

The invocation semantics remain the same.

## User-facing modes

There are 8 main modes:

| Mode | Purpose | Internal behavior |
|---|---|---|
| `quick` | Quick understanding | structure |
| `deep` | Deep reading | structure → teacher → evidence → light context |
| `internal` | Deep reading without external sources | `deep-internal` |
| `teach` | Explain methods/equations/concepts | focused teacher |
| `context` | SOTA, benchmarks, related work, author prior work, follow-ups | targeted context research |
| `critique` | Evidence and methodology stress test | evidence → targeted context as needed → critic |
| `note` | Persist notes | `compact / learning / full` |
| `full` | Complete study and archive | six-stage workflow |

If you type only:

```text
/paper-reader
```

or:

```text
/paper-reader Deep-read this paper and tell me what happened afterward.
```

the skill infers the mode from the remaining natural language.

Mode names are explicit controls, **not mandatory trigger keywords**.

## Note submodes

### Compact

```text
/paper-reader note compact
```

Save existing findings only. No new research or missing-stage execution.

### Learning

```text
/paper-reader note
```

or:

```text
/paper-reader note learning
```

Default knowledge-base format. Reuses existing analysis and adds useful light context when allowed.

### Full-format note

```text
/paper-reader note full
```

Render a Full Learning Record from the **currently verified Paper Context**. Missing analysis remains explicitly missing.

This differs from:

```text
/paper-reader full
```

which performs the complete six-stage reading workflow first and then writes the Full Learning Record.

## Natural-language routing

You can also simply ask:

```text
Quickly explain this paper.
Deep-read this paper and teach the method.
Only analyze this paper; do not use external sources.
Explain Equation 4.
Was this actually novel? What was the SOTA at the time?
What are the methodological weaknesses?
Save what we have.
Turn this into a long-term Obsidian paper note.
Read it completely and build a full learning record.
```

Explicit mode wins over inferred intent, but explicit source/network/save restrictions take precedence over mode defaults.

## Six internal capabilities

Only `paper-reader` is public:

| Capability | Responsibility |
|---|---|
| `paper-structure` | Research question, argument, method backbone, contributions, experiments, results |
| `paper-teacher` | Concepts, equations, mechanisms, step-by-step explanation |
| `paper-evidence-review` | Claim → Evidence → support strength |
| `paper-context-research` | SOTA, benchmarks, author prior work, predecessors, competitors, follow-ups, surveys, documented limitations |
| `paper-method-critic` | Experimental design, bias, confounding, statistics, reproducibility, generalization |
| `paper-note` | Compact, Learning, and Full notes |

All six reuse one shared Paper Context.

## Research depth

External context uses:

```text
none
light
targeted
full
```

- `none`: no external sources.
- `light`: minimum context needed to understand the paper; default for deep reading.
- `targeted`: deep research into one explicit question.
- `full`: broad paper-centered research map for a full learning record.

There is no fixed paper quota. Stop when the question is sufficiently answered or available evidence/tools cannot resolve the remaining gap.

## Notes

Three durable note depths are supported:

- Compact Note — save existing work only.
- Standard Learning Note — default long-term knowledge-base format.
- Full Learning Record — comprehensive format.

Unavailable material remains marked as unread / unevaluated / blocked rather than fabricated.

## Installation

### skills CLI

```bash
npx skills add https://github.com/Zhong0118/paper-reader-skill --skill paper-reader
```

### Shared skills directory

```bash
git clone https://github.com/Zhong0118/paper-reader-skill.git
cd paper-reader-skill
chmod +x install.sh
./install.sh ~/.agents/skills
```

Only one public skill is installed:

```text
~/.agents/skills/
└── paper-reader/
```

## Validation

```bash
python3 tests/validate_skills.py
```

GitHub Actions runs the same validator on pushes and pull requests.

## Design and attribution

- Architecture: [`docs/architecture.md`](docs/architecture.md)
- Workflow: [`WORKFLOW.md`](WORKFLOW.md)
- Upstream inspirations and licensing: [`ATTRIBUTION.md`](ATTRIBUTION.md)

## License

MIT.
