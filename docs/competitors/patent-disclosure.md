# patent-disclosure competitor and authority study

Date: 2026-07-05. Scope: adding `light-patent-disclosure` as an off-DAG
engineering/IP handoff skill. This document records what was actually learned
and what Light intentionally does not claim.

## Same-function skill study

| Candidate | Match quality | What was learned | What Light changed |
|---|---|---|---|
| [`handsomestWei/patent-disclosure-skill`](https://github.com/handsomestWei/patent-disclosure-skill) | Direct, high-signal Chinese patent disclosure skill; GitHub showed ~3.5k stars and MIT license | Stepwise project scan, patent-point analyzer, CNIPA-first prior-art notes, disclosure preview/build/self-check, Mermaid figures and versioned outputs | Borrow the evidence-first workflow; add `disclosure_gate.py` for source hashes, claim-support mapping, prior-art uncertainty, AI-drawing ban and overclaim block |
| [`trilogy-group/cc-skill-patent-disclosure`](https://github.com/trilogy-group/cc-skill-patent-disclosure) | Direct workflow but low public star signal | Discovery, candidate triage, interview loop, 12-section disclosure and multi-angle QC | Keep interview/QC mindset; drop Google Docs/OAuth/gogcli publishing dependency |
| [`RobThePCGuy/Claude-Patent-Creator`](https://github.com/RobThePCGuy/Claude-Patent-Creator) | Adjacent, more US/EPO application stack than disclosure-only | Phase separation: discovery, prior art, claims, specification, diagrams, abstract/front matter, compliance | Do not import MCP/BigQuery/EPO/USPTO API requirements; avoid “USPTO-ready” claims |
| [`jaccen/AI-Copyright-Skill`](https://github.com/jaccen/AI-Copyright-Skill) | Adjacent IP materials | Combined IP material framing and prior-art prompts | Use only as adjacent inspiration; Light remains general-domain and evidence-bound |

## Official/current-rule anchors

- CNIPA `专利申请受理和审批办事指南` confirms core China invention/utility-model
  application documents, language/formal constraints, electronic route and
  official acceptance logic:
  <https://www.cnipa.gov.cn/attach/0/0caf8492459846d98f3859ab05225df7.pdf>.
- CNIPA Q&A `专利申请书` is a quick official material-list reference:
  <https://www.cnipa.gov.cn/jact/front/mailpubdetail.do?sysid=6&transactId=446578>.
- WIPO Patent Drafting Manual, second edition, 2023, is the drafting-craft
  anchor for claims/descriptions/embodiment support:
  <https://www.wipo.int/publications/en/details.jsp?id=4706>.
- USPTO nonprovisional and provisional pages are cross-jurisdiction references,
  not defaults:
  <https://www.uspto.gov/patents/basics/apply/utility-patent> and
  <https://www.uspto.gov/patents/basics/apply/provisional-application>.

## Design conclusion

`light-patent-disclosure` should not pretend to be a patent attorney. Its
publicly defensible value is narrower and stronger:

1. mine technical contributions from real evidence;
2. separate technical problem, solution, effect and distinguishing features;
3. record prior-art search scope and uncertainty;
4. draft editable disclosure sections and claim/patent-point support maps;
5. produce only programmatic/vector figure sources;
6. gate the packet before saying it is ready for attorney review.

This is intentionally off-DAG: it supports a software/research project when the
user wants IP handoff materials, but it does not produce scientific findings or
reroute research stages.
