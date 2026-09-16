from pathlib import Path
import re, sys, tempfile, subprocess

ROOT = Path(__file__).resolve().parents[1]
CAPS = {
    'paper-structure': ['Paper Context', '证据', '论文类型'],
    'paper-teacher': ['Paper Context', '公式', '概念', '不要重复'],
    'paper-evidence-review': ['Paper Context', 'Claim', 'Evidence'],
    'paper-context-research': ['SOTA', 'benchmark', '作者前作', 'Survey', 'follow-up', '外部来源'],
    'paper-method-critic': ['Paper Context', '混杂', '统计', '方法学', 'external_context'],
    'paper-note': ['Paper Context', '知识库', 'Markdown', '相关论文', '技术发展脉络', 'Claim–Evidence'],
}
errors=[]

orch = ROOT/'skills'/'paper-reader'/'SKILL.md'
if not orch.exists():
    errors.append('missing skills/paper-reader/SKILL.md')
    text=''
else:
    text=orch.read_text(encoding='utf-8')
    m=re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        errors.append('paper-reader: missing YAML frontmatter')
    else:
        fm=m.group(1)
        name=re.search(r'^name:\s*(.+)$', fm, re.M)
        desc=re.search(r'^description:\s*(.+)$', fm, re.M)
        if not name or name.group(1).strip()!='paper-reader':
            errors.append('paper-reader: frontmatter name mismatch')
        if not desc or not desc.group(1).strip().startswith('Use when'):
            errors.append('paper-reader: description must start with Use when')
        if desc and len(desc.group(1))>500:
            errors.append('paper-reader: description >500 chars')

for token in [
    '唯一入口', 'quick', 'deep', 'teach', 'critique', 'archive', 'full',
    'deep-internal', 'archive-compact', 'archive-learning', 'light context', 'targeted context',
    'paper-structure', 'paper-teacher', 'paper-evidence-review',
    'paper-context-research', 'paper-method-critic', 'paper-note',
    'Paper Context', '不要重复', '外部检索'
]:
    if token not in text:
        errors.append(f'paper-reader: missing routing concept {token!r}')

for name, required in CAPS.items():
    cap = ROOT/'skills'/'paper-reader'/'capabilities'/f'{name}.md'
    if not cap.exists():
        errors.append(f'paper-reader: missing internal capability {name}')
        continue
    t=cap.read_text(encoding='utf-8')
    for token in required:
        if token not in t:
            errors.append(f'{name}: missing required concept {token!r}')
    if name != 'paper-context-research' and 'Paper Context' not in t:
        errors.append(f'{name}: no context-reuse rule')

ctx = ROOT/'skills'/'paper-reader'/'references'/'paper-context.md'
if not ctx.exists():
    errors.append('paper-reader: missing shared paper-context reference')
else:
    c = ctx.read_text(encoding='utf-8')
    for token in ['paper_internal', 'external_context', 'source_ledger', 'research_queries', 'retrieved_at', 'context_depth', 'note_depth']:
        if token not in c:
            errors.append(f'paper-context: missing {token!r}')

note = ROOT/'skills'/'paper-reader'/'capabilities'/'paper-note.md'
if note.exists():
    nt=note.read_text(encoding='utf-8')
    headings=['Compact Note', 'Standard Learning Note', 'Full Learning Record', '快速回忆','研究问题','核心公式','Claim–Evidence','技术发展脉络','作者研究路线','同期竞争','当前 SOTA','Benchmark','后续工作','推荐进一步阅读','Glossary']
    for h in headings:
        if h not in nt:
            errors.append(f'paper-note: missing rich-note section {h!r}')

# Structural depth contracts; behavioral scenarios validate the decisions.
research = ROOT/'skills'/'paper-reader'/'capabilities'/'paper-context-research.md'
if research.exists():
    rt = research.read_text(encoding='utf-8')
    for depth in ['none', 'light', 'targeted', 'full']:
        if not re.search(r'^### ' + depth + r'\s*$', rt, re.M):
            errors.append(f'paper-context-research: missing research depth {depth!r}')

# Skill-internal paths are resolved from the skill root, including references
# used by capability files. Detect broken resource links before publishing.
skill_root = ROOT/'skills'/'paper-reader'
for document in skill_root.rglob('*.md'):
    for relative in re.findall(r'(?:references|capabilities)/[a-z0-9-]+\.md', document.read_text(encoding='utf-8')):
        if not (skill_root/relative).is_file():
            errors.append(f'{document.relative_to(ROOT)}: broken resource path {relative}')

public = sorted(p.name for p in (ROOT/'skills').iterdir() if p.is_dir()) if (ROOT/'skills').exists() else []
if public != ['paper-reader']:
    errors.append(f'only paper-reader should be public, got {public}')

for path in ['README.md','README_zh.md','ATTRIBUTION.md','LICENSE','.github/workflows/validate.yml','docs/architecture.md']:
    if not (ROOT/path).exists():
        errors.append(f'missing GitHub repo file {path}')

install = ROOT/'install.sh'
if install.exists():
    with tempfile.TemporaryDirectory() as td:
        result = subprocess.run([str(install), td], cwd=ROOT, text=True, capture_output=True)
        if result.returncode != 0:
            errors.append(f'installer failed: {result.stderr.strip()}')
        installed = sorted(p.name for p in Path(td).iterdir() if p.is_dir())
        if installed != ['paper-reader']:
            errors.append(f'installer must expose only paper-reader, got {installed}')
        # Every referenced resource must survive installation byte-for-byte.
        source_root = ROOT/'skills'/'paper-reader'
        for source in source_root.rglob('*'):
            if source.is_file():
                relative = source.relative_to(source_root)
                target = Path(td)/'paper-reader'/relative
                if not target.is_file() or target.read_bytes() != source.read_bytes():
                    errors.append(f'installed package missing or changed resource {relative}')
        for name in CAPS:
            if not (Path(td)/'paper-reader'/'capabilities'/f'{name}.md').exists():
                errors.append(f'installed package missing capability {name}')
else:
    errors.append('missing install.sh')

if errors:
    print('VALIDATION FAILED')
    print('\n'.join('- '+e for e in errors))
    sys.exit(1)
print('VALIDATION PASSED: GitHub-ready six-stage paper-reader is self-contained')
