# Behavioral scenarios

These scenarios are for manual/agent evaluation in addition to structural validation.

## 1. Quick read must stay quick
User: “20 分钟帮我看懂这篇论文。”
Expected: structure only; no automatic web search or full critique.

## 2. Deep read should add context once
User: “精读这篇论文，顺便告诉我它在领域里什么位置。”
Expected: structure → teacher → evidence → light context. Related-paper searches are recorded and reused while still applicable.

## 3. Equation follow-up must reuse context
After deep read, user: “式 (4) 还是没懂。”
Expected: teacher reads existing context and only the relevant equation/method section.

## 4. Innovation requires external verification
User: “这个是不是首创？当时的 SOTA 是谁？”
Expected: targeted context research; distinguish author self-positioning from externally verified field position.

## 5. Later criticism must not rewrite the original paper
User: “后续论文说这个 benchmark 有问题，那原论文是不是也承认了？”
Expected: separate `[论文原文]` from `[后续研究]`.

## 6. Critique should consume rather than repeat search
After context research, user: “再从方法学上狠狠挑一下。”
Expected: method critic uses `external_context` and source ledger; it does not repeat the same searches.

## 7. Full learning record is explicit
User: “补齐分析并整理成完整学习档案。”
Expected: complete workflow where possible, with gaps explicitly recorded.

## 8. No web tool
User asks for current SOTA in an environment without search/web access.
Expected: report the limitation and do not invent current results.

## 9. Saving is independent of reading depth
Given: only an abstract summary exists.
User: “只把刚才内容保存成 Obsidian 笔记，不补分析。”
Expected: compact note; do not search or fabricate missing analysis.

## 10. Partial teaching is not full coverage
Given: only Equation 4 was explained.
User: “继续讲完整方法。”
Expected: reuse Eq.4 and explain remaining method sections.

## 11. A new version invalidates affected evidence
Given: cached arXiv v2; user provides v3 with changed Figure 2/results.
Expected: recheck affected claims/figures and dependent explanations, preserve unaffected content.

## 12. Unreadable figures
Given: caption readable, diagram unreadable.
Expected: caption-only evidence; no invented arrows/numbers.

## 13. Selective figure archive
Expected: save only selected core figures with version/page/caption/claim linkage and verify outputs.

## 14. Paper type matters
Given: theorem paper or survey.
Expected: use proof/review criteria rather than fabricated experimental criteria.

## 15. Internal reading does not require a literature survey
User: “只帮我读懂这篇论文的方法与证据，不查外部资料。”
Expected: structure → teacher → evidence; no external research.

## 16. Search completion is scoped and dated
Given: benchmark definitions researched previously; user asks current performance.
Expected: reuse stable definitions and refresh time-sensitive performance.

## 17. Critique revises evidence transparently
Given: a claim rated Strong; later method review finds leakage in the paper.
Expected: revise support assessment with reason/location and preserve original author claim.

## 18. Deep reading includes light context
User: “帮我深入精读这篇论文。”
Expected: structure → teacher → evidence → light context.

## 19. Explicit paper-only reading overrides defaults
User: “只帮我读懂这篇论文，不要查外部资料。”
Expected: internal/deep-internal; no external search or cached external claims in the answer.

## 20. Knowledge-base request defaults to Learning Note
User: “整理成一份以后复习用的 Obsidian 论文笔记。”
Expected: Standard Learning Note; gaps remain explicit.

## 21. Simple save remains compact
User: “把刚才内容保存一下。”
Expected: Compact Note; no new research.

## 22. Targeted can deepen full
Given: full context exists.
User: “专门查一下这个 benchmark 后来为什么被质疑。”
Expected: targeted gap-driven research; do not skip because full exists.

## 23. Old full context is not current SOTA
Given: full context from months ago.
User asks current SOTA.
Expected: refresh current performance and retrieved_at.

## 24. Learning with no external access
Given: only an abstract; no web tool.
User requests a learning note.
Expected: partial-reading Standard Learning Note; light research blocked with reason.

## 25. Persisted depth is not a global rank
Given: full research and note exist; user asks save-only, then targeted research.
Expected: compact artifact does not delete full note; targeted research retains previous full results.

## 26. Full and restrictions
User: “完整吃透并归档，但不要使用外部资料。”
Expected: internal stages and full-format note; external stage skipped with explicit restriction.

## 27. Offline cache is different from prohibited external sources
Given: verified local external sources exist; no web tool or user says “不要联网”.
Expected: dated local evidence may be reused. If user says “不要使用外部资料”, exclude it.

## 28. Explicit slash quick
User: `/paper-reader quick`
Expected: quick/structure. Do not require additional natural-language keywords.

## 29. Slash without mode uses semantic routing
User: `/paper-reader 帮我深入精读这篇论文`
Expected: infer `deep`, then structure → teacher → evidence → light context.

## 30. User-facing alias maps to internal mode
User: `/paper-reader internal`
Expected: map to `deep-internal`; no external sources.

## 31. Note defaults to learning
User: `/paper-reader note`
Expected: Standard Learning Note, equivalent to `note learning`.

## 32. note full differs from full
Given: only partial verified Context exists.

User A: `/paper-reader note full`
Expected: render Full Learning Record from current verified Context and clearly show missing sections; do not automatically run missing stages.

User B: `/paper-reader full`
Expected: attempt the six-stage workflow, then write Full Learning Record; blocked stages remain explicit.

## 33. Explicit mode yields to source restriction
User: `/paper-reader deep 不要使用外部资料`
Expected: deep-internal behavior; no external context.

## 34. Explicit note mode yields to save-only restriction
User: `/paper-reader note learning 只保存刚才已有内容`
Expected: compact behavior; no new light research.

## 35. Unknown slash token falls back to semantic routing
User: `/paper-reader 帮我看看它后续有没有被复现`
Expected: do not fail because the first Chinese token is not a mode; infer targeted context request.

## 36. Host without native slash support
Given: host loads the `paper-reader` skill but does not register `/paper-reader`.
User: “帮我精读这篇论文。”
Expected: normal natural-language routing still works; the skill does not depend on slash registration.
