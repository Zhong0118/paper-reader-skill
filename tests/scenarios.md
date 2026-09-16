# Behavioral scenarios

These scenarios are for manual/agent evaluation in addition to structural validation.

## 1. Quick read must stay quick
User: “20 分钟帮我看懂这篇论文。”
Expected: structure only; no automatic web search or full critique.

## 2. Deep read should add context once
User: “精读这篇论文，顺便告诉我它在领域里什么位置。”
Expected: structure → teacher → evidence → context research. Related-paper searches are recorded and not repeated later.

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

## 7. Archive should be rich
User: “整理成长期 Obsidian 笔记。”
Expected: comprehensive learning record containing method teaching, Claim–Evidence, methodology, technical lineage, competing/follow-up papers, SOTA/benchmark context, further-reading path, Socratic questions, glossary, and sources.

## 8. No web tool
User asks for current SOTA in an environment without search/web access.
Expected: clearly report the limitation and do not invent papers, rankings, or current results from memory.
