# Claude Code / Codex / OpenCode 兼容性说明

Light-Skills 的 canonical 技能目录是 `skills/`。为了让不同客户端不用手工复制目录，本仓库提供项目级适配桥：

```powershell
$env:PYTHONUTF8="1"
python scripts\bootstrap_agent_skills.py --mode auto --force
```

## 发现路径矩阵

| 客户端 | 公开文档中的项目级路径 | 本仓库适配 |
|---|---|---|
| Codex | `.agents/skills/<skill>/SKILL.md` | `bootstrap_agent_skills.py` 生成 `.agents/skills` |
| Claude Code | `.claude/skills/<skill>/SKILL.md` | `bootstrap_agent_skills.py` 生成 `.claude/skills` |
| OpenCode | `.opencode/skills/<skill>/SKILL.md`，也读取 `.claude/skills`、`.agents/skills` | `bootstrap_agent_skills.py` 三处都生成 |

脚本默认 `--mode auto`：优先目录 symlink，Windows 无权限时回退为 copy。copy 副本会写 `.light_generated_link`，后续可用 `--force` 安全刷新；脚本不会覆盖没有该标记的用户自建目录。

## 兼容性硬门

`bootstrap_agent_skills.py` 会检查：

- 每个技能目录必须有 `SKILL.md`。
- frontmatter 必须有 `name` 和 `description`。
- `name` 必须小写 kebab-case，且与目录名一致。
- `description` 不超过 1024 字符，避免 Claude/OpenCode 元数据加载限制。
- `name` 不包含 `claude` / `anthropic` 等保留词。

只检查不写入：

```powershell
$env:PYTHONUTF8="1"
python scripts\bootstrap_agent_skills.py --check-only --json
```

隔离自测：

```powershell
$env:PYTHONUTF8="1"
python scripts\bootstrap_agent_skills.py --selftest
```

## R/ggplot2 环境策略

`light-figure` 支持 Python/matplotlib 与 R/ggplot2 双路径。R 是增强路径，不是静默依赖：

- `python skills\light-figure\scripts\r_ggplot.py --detect` 探测 Rscript、ggplot2、scales。
- 缺 R 或缺包时，技能应先让用户选择：继续 matplotlib 诚实降级、安装/配置 R、或提供 Rscript 路径。
- 非交互自动流程默认 matplotlib 降级，并在结果中保留 `degraded=True` 与 `r_advisory`，不能假装走了 ggplot2。
- 如果交付规格写了 `required_engine=R`，降级图只能作诊断，不能作为最终交付。
