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
| `paper-note` | Compact Markdown/Obsidian notes; an expanded learning record when requested |

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

The orchestrator selects the smallest sufficient workflow and reuses verified coverage for the matching paper version. Saving is independent of reading depth: ordinary archive requests save existing findings and gaps without starting new research. Full learning records are explicitly requested.

## Installation

### skills CLI

```bash
npx skills add https://github.com/Zhong0118/paper-reader-skill --skill paper-reader
```

Use the global flag supported by your local `skills` CLI if you want it available across projects.

### Manual shared installation

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
    ├── SKILL.md
    ├── capabilities/
    │   ├── paper-structure.md
    │   ├── paper-teacher.md
    │   ├── paper-evidence-review.md
    │   ├── paper-context-research.md
    │   ├── paper-method-critic.md
    │   └── paper-note.md
    └── references/
        ├── paper-context.md
        └── figure-handling.md
```

## Search behavior

External search is **paper-centered**, not a general literature-review agent. It resolves concrete open questions; deep reading does not automatically run a literature survey. Depending on the question, it can search for:

- state of the art at publication time and today;
- benchmark definitions and known weaknesses;
- authors' directly related previous work;
- key predecessors and competing approaches;
- representative follow-up studies;
- reproduction failures, documented limitations, or contradictory evidence;
- high-quality surveys/reviews;
- official code, dataset, project, and benchmark pages.

Stop when the question is sufficiently answered, available channels cannot resolve the remaining gap, or the user’s budget is reached. There is no paper quota. Reuse stable findings and refresh time-sensitive claims.

External claims are stored separately from the target paper's own evidence and retain source metadata. If the current agent has no web/search capability, the skill must say so rather than invent related papers.

## Durable notes

Ordinary notes preserve the paper identity/version, reading coverage, research question, method, core evidence, limitations, user questions, sources and unfinished items. Saving does not fill missing sections with new research. An explicitly requested full learning record can add equations, methodology critique, research lineage, comparisons, SOTA/benchmark context, follow-ups, reading paths, understanding questions and a glossary where relevant.

## Coverage, versions and figures

The shared Context tracks each stage's scope, status and remaining work. Explaining one equation does not mark the whole method as understood. Changed paper versions trigger rechecking of affected claims, figures and dependent notes; user annotations are preserved.

View figures when an explanation depends on them, even without archiving. When saving, select core method/flow diagrams and result figures, retain figure number, page, source version, caption and claim links, and verify the saved image and note links. Caption-only access is explicitly recorded. Model redraws are labeled separately from original figures. See [`figure-handling.md`](skills/paper-reader/references/figure-handling.md).

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
