# Attribution and upstream inspirations

`paper-reader-skill` is an independently written orchestration and paper-learning workflow. It does **not** vendor or redistribute the upstream Skill files. The following projects influenced specific design ideas:

1. **flyer-Li/paper-analyst** — paper-type-aware analysis, source/evidence binding, and separating author claims from model synthesis. Upstream license: MIT.
   - https://github.com/flyer-Li/paper-analyst

2. **zsyggg/paper-craft-skills (`paper-analyzer`)** — teaching-oriented explanation of methods, equations, mechanisms, and prerequisites. The upstream repository README states `License: MIT`; this repository does not copy its Skill text.
   - https://github.com/zsyggg/paper-craft-skills

3. **bytedance/deer-flow (`academic-paper-review`)** — claim-to-evidence review and literature-context checks. Upstream license: MIT.
   - https://github.com/bytedance/deer-flow

4. **K-Dense-AI/scientific-agent-skills (`scientific-critical-thinking`)** — methodological critique, bias/confounding, statistics, evidence quality, and claim evaluation. Upstream license: MIT.
   - https://github.com/K-Dense-AI/scientific-agent-skills

5. **917Dhj/DeepPaperNote** — durable single-paper notes, argument reconstruction, grounding, and long-term knowledge-base orientation. Upstream license: MIT.
   - https://github.com/917Dhj/DeepPaperNote

The implementation in this repository was rewritten around a shared Paper Context and single-entry orchestration model to avoid repeated full-paper analysis. Upstream names remain trademarks/names of their respective owners.
