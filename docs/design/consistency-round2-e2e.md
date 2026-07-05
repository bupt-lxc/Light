# consistency Round 2 活体 E2E 证据（2026-07-01）

## 输入与上游读取证据

- 公开论文：Vaswani et al., *Attention Is All You Need*，
  `https://arxiv.org/pdf/1706.03762`
- PDF SHA-256：`BDFAA68D8984F0DC02BEACA527B76F207D99B666D31D1DA728EE0728182DF697`
- `pdf_ops triage`：`born_digital`；15/15 页文本层，image-only=0，sparse=0
- parse-once 后目标读取：p.1 Abstract、p.7 §5.1、p.8 Table 2 与 §6.1
- p.8 视觉复核：`Transformer (big)` 行的 EN-DE BLEU 为 **28.4**，同一行 EN-FR 为 41.8；
  页面 PNG SHA-256：
  `9A65FDAA6A2121AFAE12AA7488461B6094D2F6CC46538DCDD332E7C685421480`
- 未读：p.2–6、p.9–15 正文；本次只核方法名、数据集、EN-DE 主指标与原论文 claim，不宣称全文事实全覆盖

## 临时权威源

在 `.upgrade/_e2e/.light/consistency` 建四份完整 registry，所有 authority 均为：

- `owner: memory-pm`
- `updated_at: 2026-07-01`
- canonical / record / claim 均有 `status=confirmed + source + locator`

主记录：

```text
Transformer (big) × WMT 2014 English-German → BLEU 28.4
locator = p.8 Table 2, row Transformer (big), BLEU EN-DE
```

## before：真冲突与阻断

两份现实交付物：

- `abstract.md`：正确写 `Transformer (big)` / 28.4 BLEU
- `README.md`：故意漂移为 `TransformerNet`、`Transformer-big`、24.8 BLEU

实跑结果：

- `consistency_audit --report`：4 条 finding
  - 2 × `SUBSTITUTION`
  - 2 × `METRIC_VALUE`
- `AUTHORITY_COVERAGE`：0 条（权威链完整）
- findings schema validate：通过
- audit exit：**1**
- `run_checkpoint --stage 8 --write`：**exit 1**
- passport：`stage[8].gate=FAIL`，`status=gate_failed`

## 人裁与真修

裁定依据是论文 p.8 Table 2 的文本抽取 + 页面视觉回看，不是“为了让测试变绿”：

- 权威源 28.4 正确；
- 应把 README 改回 `Transformer (big)` / 28.4；
- 不更新权威源，不把 24.8 晋升为新真值。

## after：全量复扫

修 README 后，对同一 scan set 复跑：

- findings：0
- `verdict=pass`
- audit exit：**0**
- checkpoint exit：**0**
- passport：`stage[8].gate=PASS`，`status=delivered`

本 E2E 证明的仅是：

```text
真实 PDF locator/coverage
→ 经确认的 .light 权威源
→ 跨两份交付物 findings
→ checkpoint 真阻断
→ 按原论文裁定修复
→ 同 scan set 复扫转绿
```

它不证明未读页面、未列入 scan set 的材料或 2026 当前机器翻译 SOTA 已核。
