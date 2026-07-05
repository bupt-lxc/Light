# software-copyright competitor and authority study

Date: 2026-07-05. Scope: adding `light-software-copyright` as an off-DAG
engineering/IP material-preparation skill for China software copyright drafts.

## Same-function skill study

| Candidate | Match quality | What was learned | What Light changed |
|---|---|---|---|
| [`Fokkyp/SoftwareCopyright-Skill`](https://github.com/Fokkyp/SoftwareCopyright-Skill) | Direct and high-signal; GitHub showed ~4.2k stars, MIT license | Actual skill lives in `software-copyright-materials/`; strong mechanisms include real-project analysis, application worksheet, business-context/manual drafting, front/back 30 source extraction, user confirmation gates and formal output folder | Borrow the staged material flow; add stricter `materials_gate.py` for source hashes, version consistency, confirmations, page/line rules, secret scan and no-submission/no-guarantee boundaries |
| [`na57/chinese-copyright-application-skill`](https://github.com/na57/chinese-copyright-application-skill) | Direct China soft-copyright skill, lower star signal | Useful field/template checklist for application form, source code and manual | Treat as checklist only; Light requires provenance and confirmation gates |
| [`jaccen/AI-Copyright-Skill`](https://github.com/jaccen/AI-Copyright-Skill) | Adjacent combined IP skill | IP material packaging and references | Avoid AI-generated-code or one-size IP assumptions |

## Official/current-rule anchors

- National Copyright Administration `计算机软件著作权登记办法`:
  <https://www.ncac.gov.cn/xxfb/flfg/bmgz/202410/P020241015604759788122.pdf>.
  It anchors applicant/material categories, China Copyright Protection Center,
  identification material, front/back 30 pages, all-material rule under 60
  pages, line-count norms and Chinese/A4 form requirements.
- Beijing government service guide `计算机软件著作权登记初审`:
  <https://banshi.beijing.gov.cn/pubtask/task/1/110000000000/3e283672-76be-4c8c-98e8-0bebe9bd06bf.html?locationCode=110000000000>.
  It consolidates current service expectations such as version consistency,
  signatures/seals and document printing norms.
- U.S. Copyright Office Circular 61:
  <https://www.copyright.gov/circs/circ61.pdf>.
  It is only a non-CN comparison; US computer-program deposit rules differ.

## Design conclusion

The user value is not “AI writes a soft-copyright package.” The defensible
product value is:

1. inspect real source and select deposit material without fabricating code;
2. keep application worksheet, manual, source headers and filenames consistent;
3. enforce staged confirmation before formal export;
4. respect front/back or all-material page rules;
5. block secrets/private data before source-code material leaves the project;
6. output local review materials, not registration guarantees or submission.

This skill remains off-DAG because registration material preparation is an
engineering/IP handoff task, not a scientific research stage.
