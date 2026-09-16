# Paper Reader Skill

[中文说明](README_zh.md)

A single-entry Agent Skill for **deep paper reading and learning**. It does more than summarize one PDF: it teaches the method, audits claim-to-evidence support, searches the surrounding literature, critiques methodology, and produces a durable research note.

## What it does

`paper-reader` is the only public skill. Internally it orchestrates six capabilities around one shared Paper Context:

| Capability | Responsibility |
|---|---|
| `paper-structure` | Research question, argument, method backbone, contributions, experiments, results |
| `paper-teacher` | Concepts, equations, mechanisms, and step-by-step explanation |
| `paper-evidence-review` | Claim → Evidence → support strength |
| `paper-context-research` | SOTA, benchmarks, author prior work, predecessors, competitors, follow-ups, surveys, externally documented limitations |
| `paper-method-critic` | Experimental design, bias, confounding, statistics, reproducibility, generalization |
| `paper-note` | A comprehensive Markdown/Obsidian learning record with related-paper comparisons |

The six capabilities **reuse the same context**. They are not six independent agents rereading the paper from scratch.

## Natural-language routing

You normally just ask:

```text
Quickly explain what this paper does.
Deep-read this paper and teach it to me.
Explain Equation 4 and why it is designed this way.
Does the evidence really support the main claim?
Find the SOTA, benchmark context, author prior work, follow-up papers and surveys around this paper.
What are the methodological weaknesses, including limitations found by later papers?
Turn everything into a durable Obsidian note.
Read this paper completely and build a full learning record.
```

The orchestrator selects the smallest sufficient workflow and reuses completed stages.

## Installation

### skills CLI

```bash
npx skills add https://github.com/<YOUR_GITHUB_USERNAME>/paper-reader-skill --skill paper-reader
```

Use the global flag supported by your local `skills` CLI if you want it available across projects.

### Manual shared installation

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/paper-reader-skill.git
cd paper-reader-skill
chmod +x install.sh
./install.sh ~/.agents/skills
```

Only one public skill is installed:

```text
~/.agents/skills/
└── paper-reader/
    ├── SKILL.md
    ├── capabilities/
    │   ├── paper-structure.md
    │   ├── paper-teacher.md
    │   ├── paper-evidence-review.md
    │   ├── paper-context-research.md
    │   ├── paper-method-critic.md
    │   └── paper-note.md
    └── references/
        └── paper-context.md
```

## Search behavior

External search is **paper-centered**, not a general literature-review agent. In deep/full/context/critique workflows it can search for:

- state of the art at publication time and today;
- benchmark definitions and known weaknesses;
- authors' directly related previous work;
- key predecessors and competing approaches;
- representative follow-up studies;
- reproduction failures, documented limitations, or contradictory evidence;
- high-quality surveys/reviews;
- official code, dataset, project, and benchmark pages.

External claims are stored separately from the target paper's own evidence and retain source metadata. If the current agent has no web/search capability, the skill must say so rather than invent related papers.

## Durable notes

`paper-note` creates a learning record rather than an abstract rewrite. It includes method explanations, equations, Claim–Evidence, methodology critique, research lineage, author trajectory, competing work, SOTA/benchmark context, follow-up papers, surveys, a further-reading path, Socratic questions, a glossary, and a source ledger.

## Validation

```bash
python3 tests/validate_skills.py
```

GitHub Actions runs the same validator on pushes and pull requests.

## Publish this repository

After editing the repository name/description as you like:

```bash
git init -b main
git add .
git commit -m "feat: initial paper-reader skill"
gh repo create paper-reader-skill --public --source=. --remote=origin --push
```

Or run `./publish.sh paper-reader-skill public` after authenticating `gh`.

## Design and attribution

- Architecture: [`docs/architecture.md`](docs/architecture.md)
- Workflow: [`WORKFLOW.md`](WORKFLOW.md)
- Upstream inspirations and licensing: [`ATTRIBUTION.md`](ATTRIBUTION.md)

This repository contains an independently written orchestration and capability set; it does not vendor the upstream Skill files.

## License

MIT. See [`LICENSE`](LICENSE).
