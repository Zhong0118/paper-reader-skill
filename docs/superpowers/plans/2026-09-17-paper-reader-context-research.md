# Paper Reader Context Research Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade paper-reader into a GitHub-ready single-entry paper learning skill with six internal capabilities, including scoped web research and a comprehensive durable note.

**Architecture:** `paper-reader` remains the only public skill. Six internal capabilities share one Paper Context; external research is isolated in `external_context` and performed once per relevant workflow, then reused by critique and note stages. The repository is installable from its `skills/paper-reader` directory and includes validation, attribution, and publishing guidance.

**Tech Stack:** Markdown Agent Skills, Bash installer, Python validation, Git/GitHub.

**Spec:** `docs/architecture.md`

## Global Constraints
- Only `paper-reader` is publicly registered under `skills/`.
- Paper facts and external literature facts must never be merged without source labels.
- External research is scoped around the current paper; it is not a general literature-review agent.
- Existing Paper Context is reused; no capability repeats full-paper analysis without a concrete gap.
- Notes must be useful for long-term study, not abstract rewrites.

---

### Task 1: Extend validation for the six-stage workflow
**Files:** Modify `tests/validate_skills.py`; modify `tests/scenarios.md`.
- [ ] Add failing checks for `paper-context-research`, external context schema, web research routing, and rich notes.
- [ ] Run validator and confirm it fails against the old package.

### Task 2: Extend Paper Context and research capability
**Files:** Modify `skills/paper-reader/references/paper-context.md`; create `skills/paper-reader/capabilities/paper-context-research.md`.
- [ ] Add `external_context`, source ledger, query ledger, and freshness metadata.
- [ ] Define scoped searches for SOTA, benchmark, author prior work, predecessors, competing/follow-up work, surveys, limitations, and contradictory evidence.
- [ ] Require citation-quality and temporal-context checks.

### Task 3: Update orchestration and downstream capabilities
**Files:** Modify `skills/paper-reader/SKILL.md`, `paper-evidence-review.md`, `paper-method-critic.md`, `paper-note.md`.
- [ ] Route `deep`, `critique`, `archive`, and `full` through context research when useful.
- [ ] Make critic consume internal and external evidence without duplicating search.
- [ ] Expand note into a paper learning record with related-work comparisons and reading path.

### Task 4: Make repository GitHub-ready
**Files:** Rewrite `README.md`; create `README_zh.md`, `docs/architecture.md`, `ATTRIBUTION.md`, `.gitignore`, `LICENSE`, `.github/workflows/validate.yml`.
- [ ] Document installation from GitHub and manual installation.
- [ ] Document upstream inspirations and licensing constraints without redistributing unlicensed source text.
- [ ] Add CI validation.

### Task 5: Verify and package
**Files:** `install.sh`, repository archive.
- [ ] Run Python validation.
- [ ] Run installer smoke test.
- [ ] Initialize a local git repository and create an initial commit.
- [ ] Create `paper-reader-skill.zip` excluding `.git` and temporary artifacts.
