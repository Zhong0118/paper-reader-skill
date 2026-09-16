# Changelog

## 0.4.1 - 2026-09-17

- Added a clear explicit invocation convention: `/paper-reader <mode> <request>`.
- Added eight user-facing modes: quick, deep, internal, teach, context, critique, note, and full.
- Kept natural-language semantic routing when no mode is supplied.
- Added note submodes: compact, learning, and full.
- Clarified that `note full` renders the current verified Context, while `full` runs the complete six-stage workflow first.
- Clarified that slash availability depends on the host; the repository remains a portable Agent Skill and does not vendor host-specific command adapters.
- Added precedence rules for explicit modes versus source/network/save restrictions.
- Added behavioral scenarios and validator checks for slash-aware invocation.

## 0.4.0 - 2026-09-17

- Added external research depths: none / light / targeted / full; deep defaults to light context.
- Added explicit deep-internal reading and source-restriction precedence.
- Added compact / learning / full notes; knowledge-base and Obsidian requests default to Standard Learning Note.
- Kept save-only requests compact without new analysis or research.
- Separated requested depth from actual execution/coverage and note artifacts.
- Preserved targeted follow-ups and freshness checks even after full research, without paper quotas.
- Retained version invalidation, scoped stages, selective figure handling and paper-type-aware critique.

## 0.3.0 - 2026-09-17

- Separated reading depth from archiving; compact notes save existing findings and gaps, while full records are explicit.
- Added scoped stage status, source versions and dependent-evidence revision rules.
- Made external research question-driven with incremental refresh and stopping conditions.
- Added shared figure viewing, selective preservation, provenance and output verification guidance.
- Clarified evidence ratings, abstract-only limits, theory/survey critique, and expanded behavioral scenarios.

## 0.2.0 - 2026-09-17

- Added `paper-context-research` as the sixth internal capability.
- Added paper-centered web/literature research for SOTA, benchmarks, author prior work, predecessors, competitors, follow-ups, surveys, limitations, and contradictory findings.
- Separated `paper_internal` and `external_context` in the shared Paper Context.
- Expanded `paper-note` into a full paper learning record with research lineage, comparisons, reading paths, Socratic questions, glossary, and source ledger.
- Added GitHub-ready documentation, validation workflow, MIT license, and upstream attribution.

## 0.1.0 - 2026-09-16

- Initial five-capability orchestrated paper-reader prototype.
