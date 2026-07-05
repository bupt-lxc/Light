# data-engineering Round 2 活体 E2E（2026-07-02）

## 场景

研究者要为乳腺癌二分类基线找一个公开表格数据集，但不能“看到标题就下载”：先用公开资源发现候选，
核许可/版本/大小/split，再锁 revision 下载、画像、清洗、划分、查泄漏、判可行性并交 stage-2 checkpoint。

## 真联网来源与快照

- provider：Hugging Face 公开 Dataset API（免 key 元数据）
- dataset id：`scikit-learn/breast-cancer-wisconsin`
- revision：`e41c086f1614397ce7a5660980aac421047cef5e`
- file：`breast_cancer.csv`
- source URL：`https://huggingface.co/datasets/scikit-learn/breast-cancer-wisconsin/resolve/e41c086f1614397ce7a5660980aac421047cef5e/breast_cancer.csv`
- HF card 声明 license：`cc-by-sa-4.0`
- raw SHA256：`27f219231dbb30eecbfc1361407ed641ea01be43316e2c707a1baf82c9795e23`
- cleaned SHA256：`8eb50040833604b43dbf8ce129e32a5002d31d052e0477bd352d7886ff68f2ed`

`dataset_intake.py --query "breast cancer" --limit 5 --sort downloads` 真返回候选，并把该候选判为
`review` 而不是 usable：许可和 revision 可核，但官方 split 元数据缺失，须自行设计并记录。

## 真抓真修

### 1. 抓到真实源数据质量问题

下载文件每行末尾多一个空字段，pandas 读成全空 `Unnamed: 32`：

- raw shape：`569 × 33`
- `data_doctor` 真实命中全空列 `Unnamed: 32`
- 同时识别 `id` 为 ID-like 观察单位标识

修法不是为了绿而乱删：只删除可由原文件逐字确认的全空导出尾列，保留 `id` 作为患者级 split/provenance
标识；clean shape 为 `569 × 32`，并记录 raw/clean 两个 SHA256。

### 2. 活体发现并修复现有 `data_doctor` bug

第一次跑真实 WDBC 时，`diagnosis` 是字符串分类标签 `M/B`；旧代码虽准备走分类分支，却先执行
`float("M").is_integer()`，触发 `ValueError`。旧 selftest 只覆盖数字 0/1 标签，所以 11/11 绿未暴露。

修复范围最小：

- 仅当 target 本身是数值列时才判断“低基数整数编码分类”；
- 新增字符串 `M/B` 分类目标回归，继续要求数值泄漏特征与类别泄漏特征均可命中；
- 不改其余画像、阈值、severity 或 findings 接线。

### 3. 真阻断跨 split 污染，再按根因修

用固定 `random_state=42`、按 `diagnosis` 分层划分后，模拟真实常见误操作：把一名训练患者追加进 test。

`split_leakage.py --group-col id --target diagnosis` 真命中：

- `exact_duplicate`
- `entity_overlap`

脚本 exit `1`，`run_checkpoint --stage 2 --write` 真 exit `1`，passport 变为 `gate_failed`。

随后删除错误注入，保持原固定 split，复跑：

- leakage gate exit `0`
- 实际 `n=569`、两类计数与 30 个模型特征进入 `data_feasibility_gate`
- feasibility verdict=`pass`、exit `0`
- checkpoint exit `0`
- passport 最终 `delivered`
- `passport validate` exit `0`

## 回归判据

本 E2E 证明的不是“这个数据集适合所有乳腺癌研究”，只证明下列链路真实成立：

1. 公开 API 发现候选且缺字段不假装 usable；
2. revision-locked 真下载与 SHA256 血缘；
3. 真实画像抓源文件问题；
4. 字符串分类目标不再让 `data_doctor` 崩溃；
5. 跨 split 重复/实体污染能产 critical findings；
6. stage-2 checkpoint 会真阻断；
7. 按根因修复后泄漏、可行性、checkpoint 与 passport 全链放行。

临时产物位于 `.upgrade/_e2e/data-engineering-round2`，完成后已删除；本文件是永久审计证据。
