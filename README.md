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
| `paper-note` | Compact saves, standard learning notes, and full learning records |

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

## Reading modes and notes

- Quick look: the paper's structure.
- Deep reading: explanation and Claim–Evidence plus **light research context** by default: key predecessors, what changed, representative follow-ups and a useful survey.
- Paper-only reading: say “do not use external sources” to suppress external context.
- Full learning record: all six capabilities, adapted to the paper and available evidence.

Three note formats are separate from reading depth:

| Request | Format |
|---|---|
| “Save what we have” | Compact Note; no new research or analysis |
| “Make an Obsidian paper note for later study” | Standard Learning Note; useful light context added when allowed |
| “Read it fully and archive everything” | Full Learning Record |

Explicit “save existing content only” remains compact even when Obsidian is mentioned. Learning notes retain unread/unevaluated gaps rather than pretending a complete reading has occurred.

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

External search is **paper-centered**, not a general literature-review agent. Deep reading defaults to light, paper-centered context rather than a broad literature survey. Research can be none, light, targeted or full. Targeted research can deepen one question even after full research. Depending on the question, it can search for:

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

Compact notes save existing findings, reading coverage, sources and unfinished items without new analysis. Standard Learning Notes organize methods and key equations, evidence, limitations, research context, important related-paper comparisons, user questions, reading paths and sources. They supplement useful light context when permitted. Full Learning Records can further expand methodology critique, author trajectory, SOTA/benchmark context, understanding questions and glossary sections.

Unavailable material or search tools are reported as gaps. Explicit source restrictions override defaults. Depth labels describe work actually performed, not proof that every section is complete.

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
