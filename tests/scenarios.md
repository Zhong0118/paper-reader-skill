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
Given: only an abstract summary exists. User: “整理成长期 Obsidian 笔记。”
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
User: “只帮我读懂这篇论文的方法与证据。”
Expected: structure, teacher and internal evidence review; external research only if needed to resolve a concrete prerequisite, honoring explicit no-web instructions.

## 16. Search completion is scoped and dated
Given: benchmark definitions researched previously; user now asks about current performance.
Expected: reuse stable definitions, refresh time-sensitive performance, record settings and unresolved questions. No fixed paper quota; no inference that absent search results prove absence of contrary findings.

## 17. Critique revises evidence transparently
Given: a claim rated Strong; a methodological review finds test leakage in the paper.
Expected: revise the associated support assessment with location/reason, invalidate dependent summary/note statements, preserve the original author claim and user annotations.
