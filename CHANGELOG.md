# Changelog

## 0.5.0 - 2026-09-17

- Added `compare` as the ninth user-facing mode and `paper-compare` as the seventh internal capability.
- Added Collection support for folders and defined paper sets with manifest, normalized comparison, and synthesis outputs.
- Added large-folder inventory/triage behavior so multi-paper workflows do not default to `full × N`.
- Added comparison coverage semantics: reported / derived / not_reported / not_assessed / not_accessible / not_applicable / uncertain.
- Added `context_revision` and `note_sync` (`auto / on-demand / off`) for durable incremental Note synchronization.
- Added managed/user Markdown regions so Paper Reader can merge model-maintained sections while preserving user-authored content.
- Added section-aware Note merge/revise/deduplicate behavior instead of whole-file replacement or chat-style append.
- Added incremental collection updates: new/changed papers patch affected rows/cells and dependent synthesis only.
- Kept collection-level comparison separate from single-paper Notes.
- Expanded behavioral validation for note sync, folder triage, provenance, cross-paper comparison, and natural-language compare routing.

## 0.4.1 - 2026-09-17

- Added the `/paper-reader <mode>` explicit invocation convention while preserving natural-language routing.
- Added user-facing quick / deep / internal / teach / context / critique / note / full modes.
- Clarified `note full` versus full workflow.

## 0.4.0 - 2026-09-17

- Added external research depths: none / light / targeted / full; deep defaults to light context.
- Added explicit deep-internal reading and source-restriction precedence.
- Added compact / learning / full notes.
- Separated requested depth from actual execution/coverage.

## 0.3.0 - 2026-09-17

- Added scoped stage status, source versions, figure handling, and question-driven research.

## 0.2.0 - 2026-09-17

- Added paper-centered external research and rich learning records.

## 0.1.0 - 2026-09-16

- Initial orchestrated paper-reader prototype.
