# IP extension live gate

Date: 2026-07-05.

Scope: add two off-DAG engineering/IP handoff skills after Round 3:

- `light-patent-disclosure`
- `light-software-copyright`

These skills are not scientific DAG stages. They do not enter
`STAGE_GATES`, `ROUTES` or `light.findings.v1`, and they do not provide legal
advice, file applications, submit materials or guarantee patent/copyright
outcomes.

## External learning record

Same-function and authority sources reviewed before implementation:

- `handsomestWei/patent-disclosure-skill` — high-signal Chinese patent
  disclosure workflow: project scan, patent-point mining, prior-art notes,
  editable disclosure draft, Mermaid figures and self-check.
- `Fokkyp/SoftwareCopyright-Skill` — high-signal Chinese software copyright
  material workflow: real-project source extraction, application worksheet,
  manual drafting, confirmation stops and formal-output folder.
- Adjacent/contrast projects: `trilogy-group/cc-skill-patent-disclosure`,
  `RobThePCGuy/Claude-Patent-Creator`, `na57/chinese-copyright-application-skill`,
  `jaccen/AI-Copyright-Skill`.
- Official/high-trust anchors: CNIPA patent application guide and Q&A, WIPO
  Patent Drafting Manual, USPTO utility/provisional filing pages, National
  Copyright Administration `计算机软件著作权登记办法`, Beijing software copyright
  service guide, U.S. Copyright Office Circular 61.

Detailed notes:

- [`docs/competitors/patent-disclosure.md`](../competitors/patent-disclosure.md)
- [`docs/competitors/software-copyright.md`](../competitors/software-copyright.md)
- [`skills/light-patent-disclosure/references/patent-resource-map.md`](../../skills/light-patent-disclosure/references/patent-resource-map.md)
- [`skills/light-software-copyright/references/software-copyright-resource-map.md`](../../skills/light-software-copyright/references/software-copyright-resource-map.md)

## Commands personally run

All commands were run on Windows with `PYTHONUTF8=1` from repository root
`D:\skill\Light-Skills`.

```powershell
python skills\light-patent-disclosure\scripts\disclosure_gate.py --selftest
```

Result: exit 0.

```text
[OK] valid packet passes
[OK] guarantee language fails
[OK] AI drawing fails
[OK] hash mismatch fails
[OK] filing overstep fails
```

```powershell
python skills\light-software-copyright\scripts\materials_gate.py --selftest
```

Result: exit 0.

```text
[OK] valid CN materials packet passes
[OK] version mismatch fails
[OK] AI/fake code source fails
[OK] front/back page rule fails
[OK] secret scan failure blocks export
```

```powershell
python $env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\light-patent-disclosure
python $env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\light-software-copyright
```

Result: both exit 0, `Skill is valid!`.

```powershell
$skills = Get-ChildItem -Path skills -Directory -Filter 'light-*' | Sort-Object Name
foreach ($skill in $skills) {
  python $env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py $skill.FullName
}
```

Result: 23 checked, 0 failed.

```powershell
python skills\light-orchestrator\scripts\integration_audit.py --selftest
python skills\light-orchestrator\scripts\integration_audit.py --root .
```

Result: both exit 0; live integration inventory reports 23 skills and PASS.

```powershell
python -m py_compile `
  skills\light-patent-disclosure\scripts\disclosure_gate.py `
  skills\light-software-copyright\scripts\materials_gate.py `
  skills\light-orchestrator\scripts\integration_audit.py `
  skills\light-orchestrator\resident\session_start_resident.py
```

Result: exit 0.

## Integration result

Current public inventory:

- controller: 1 (`light-orchestrator`)
- resident overlays: 5
- research pipeline stages: 13
- engineering/IP off-DAG skills: 4

The two new IP skills are intentionally off-DAG:

- `light-patent-disclosure`: prepares evidence-backed patent disclosure packets
  for attorney/patent-agent review and blocks grant/filing guarantees, AI
  patent drawings, unsupported claim elements and stale/missing hashes.
- `light-software-copyright`: prepares China software copyright material drafts
  from real project source and blocks fabricated code, page-rule mismatches,
  unconfirmed fields, version drift, secret-scan failures and submission
  guarantees.

## Honest non-claims

- No real patent filing, copyright registration, office submission, payment,
  DOCX filing upload or attorney/legal review was performed.
- Official legal and portal requirements can change; real use must recheck
  current official sources on the day of use.
- Passing these gates means the local material packet is internally auditable
  and ready for user/professional review; it does not mean the application will
  be accepted, granted or registered.
