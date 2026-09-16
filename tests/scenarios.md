# Behavioral scenarios

These scenarios are for manual/agent evaluation in addition to structural validation.

## 1. Quick read must stay quick
User: “20 分钟帮我看懂这篇论文。”
Expected: structure only; no automatic web search or full critique.

## 2. Deep read should add context once
User: “精读这篇论文，顺便告诉我它在领域里什么位置。”
Expected: structure → teacher → evidence → context research. Related-paper searches are recorded and reused while still applicable; time-sensitive follow-ups may refresh them.

## 3. Equation follow-up must reuse context
After deep read, user: “式 (4) 还是没懂。”
Expected: teacher reads the existing context and only the relevant equation/method section.

## 4. Innovation requires external verification
User: “这个是不是首创？当时的 SOTA 是谁？”
Expected: context research; answer distinguishes author self-positioning from externally verified field position.

## 5. Later criticism must not rewrite the original paper
User: “后续论文说这个 benchmark 有问题，那原论文是不是也承认了？”
Expected: separate `[论文原文]` from `[后续研究]`; never attribute later criticism to the target paper unless it actually appears there.

## 6. Critique should consume rather than repeat search
After context research, user: “再从方法学上狠狠挑一下。”
Expected: method critic uses `external_context` and source ledger; it does not run the same SOTA/survey searches again.

## 7. Full learning record is explicit
User: “补齐分析并整理成完整学习档案。”
Expected: comprehensive learning record containing method teaching, Claim–Evidence, methodology, technical lineage, competing/follow-up papers, SOTA/benchmark context, further-reading path, Socratic questions, glossary, and sources.

## 8. No web tool
User asks for current SOTA in an environment without search/web access.
Expected: clearly report the limitation and do not invent papers, rankings, or current results from memory.

## 9. Saving is independent of reading depth
Given: only an abstract summary exists. User: “只把刚才内容保存成 Obsidian 笔记，不补分析。”
Expected: save the existing summary and its coverage/gaps; do not search or fabricate method, critique, or related work to fill a template.

## 10. Partial teaching is not full coverage
Given: legacy completed_stages includes teacher, but only Equation 4 was explained.
User: “继续讲完整方法。”
Expected: inspect actual coverage, reuse Equation 4, explain remaining method sections, record scope and remaining items rather than skipping teacher.

## 11. A new version invalidates affected evidence
Given: cached arXiv v2; user provides v3 with changed Figure 2 and results.
Expected: record versions, recheck affected claims/figures and dependent explanations; preserve unaffected verified content. Do not silently reuse v2 or overwrite user notes.

## 12. Unreadable figures
Given: Figure 2 caption is readable, but the diagram is not. User asks about arrows and saving it.
Expected: report caption-only evidence; no invented arrows/numbers. Try available rendering; if unavailable, retain locator and gap, never claim an image was saved or visually verified.

## 13. Selective figure archive
Given: method figure, core ablation, and decorative images. User requests a note with key figures.
Expected: preserve selected complete figures, source version/page/caption/claim links; verify saved images and note links; distinguish original crops from model redraws.

## 14. Paper type matters
Given: a theorem paper or a survey. User requests critique.
Expected: evaluate assumptions/proof coverage or search/selection/synthesis respectively; do not invent datasets or demand seeds and randomized trials.

## 15. Internal reading does not require a literature survey
User: “只帮我读懂这篇论文的方法与证据，不查外部资料。”
Expected: structure, teacher and internal evidence review; no external research; external prerequisites remain explicit gaps.

## 16. Search completion is scoped and dated
Given: benchmark definitions researched previously; user now asks about current performance.
Expected: reuse stable definitions, refresh time-sensitive performance, record settings and unresolved questions. No fixed paper quota; no inference that absent search results prove absence of contrary findings.

## 17. Critique revises evidence transparently
Given: a claim rated Strong; a methodological review finds test leakage in the paper.
Expected: revise the associated support assessment with location/reason, invalidate dependent summary/note statements, preserve the original author claim and user annotations.

## 18. Deep reading includes light context
User: “帮我深入精读这篇论文。”
Expected: structure → teacher → evidence → light context. Attempt key predecessors, differences, useful follow-ups and surveys without quotas or broad SOTA scans.

## 19. Explicit paper-only reading overrides defaults
User: “只帮我读懂这篇论文，不要查外部资料。”
Expected: deep-internal; no external search or external cached facts in this answer. Preserve existing external records without using them.

## 20. Knowledge-base request defaults to Learning Note
User: “整理成一份以后复习用的 Obsidian 论文笔记。”
Expected: Standard Learning Note using available methods, evidence, limitations, useful light context, comparisons, reading path and sources. Internal reading gaps are explicit, not fabricated or silently marked complete.

## 21. Simple save remains compact
User: “把刚才内容保存一下。”
Expected: Compact Note; no missing-stage execution or new research. The same holds for “只保存刚才内容到 Obsidian”.

## 22. Targeted can deepen full
Given: full context exists. User: “专门查一下这个 benchmark 后来为什么被质疑。”
Expected: targeted gap-driven research, reusing relevant reliable evidence; do not skip because a full label exists.

## 23. Old full context is not current SOTA
Given: full context from months ago. User asks current SOTA.
Expected: refresh current performance and retrieved_at; retain stable benchmark definitions.

## 24. Learning with no external access
Given: only an abstract; no web tool. User requests a learning note.
Expected: partial-reading Standard Learning Note, no fabricated methods or citations; light research blocked with a reason. Do not set context_depth=light solely because it was planned.

## 25. Persisted depth is not a global rank
Given: full research and full note exist; user asks save-only, then targeted research.
Expected: compact artifact updates note metadata without deleting full note; saving does not alter research coverage. Targeted research updates its actual scope while retaining previous full results.

## 26. Full and restrictions
User: “完整吃透并归档，但不要使用外部资料。”
Expected: internal stages and full note, external research skipped with a stated restriction; no false claim that all six stages completed. The restriction also overrides learning defaults.

## 27. Offline cache is different from prohibited external sources
Given: verified local external sources exist; no web tool or user says “不要联网”.
Expected: reuse permitted, dated local evidence; mark only unmet online verification blocked. If user instead says “不要使用外部资料”, exclude cached external claims from the answer while preserving the stored records.
