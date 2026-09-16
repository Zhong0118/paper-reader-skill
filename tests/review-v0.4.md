# v0.4 validation

Baseline instruction simulation found the two intended gaps: deep did not default to light context, and Obsidian study notes routed to compact. Save-only, source restrictions and targeted follow-ups already worked and remain supported.

Revised instruction simulations passed scenarios 18–26. A follow-up check of scenario 27 confirmed the corrected distinction between prohibited external sources and unavailable/prohibited networking: permitted dated local evidence remains reusable only in the latter case. Unknown legacy depth is left absent with pending coverage recorded rather than assigned a false completion label.

Checks performed:

- Repository validator failed on the missing v0.4 depth/routing contracts before implementation, then passed after implementation.
- Skill-creator metadata validator passed.
- Skills CLI discovery found exactly one public skill; isolated temporary-directory installation succeeded for Codex.
- Temporary installation preserved package resources; reference paths resolved.
- Git diff whitespace check passed.

These are structural checks and instruction-level simulations, not real-PDF reading, image extraction or live literature-search evaluations. v0.3 figure handling and paper-type critique files were retained unchanged.
