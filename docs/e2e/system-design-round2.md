# system-design Round 2 live E2E

Date: 2026-07-03 (Asia/Shanghai)

Repository baseline: `3de0ba873ea0f364bb38d35f67c8ae95f329ed5a` on `main`

Runtime: Python 3.11.13, stdlib SQLite 3.45.3, Windows

## Scope and protection

The rehearsal used only
`<repo>\.upgrade\_e2e\system-design-round2`. No production
database, configuration, `_shared`, orchestrator gate, route, or other skill
implementation was changed.

The source fixture was a realistic existing research experiment tracker:

- one Python HTTP process and SQLite database;
- `tenant`, `app_user`, `experiment_run`, and `run_event` tables;
- `app_user.email` PII and application-enforced tenant boundaries;
- REST `/v1/runs`;
- a legacy client that requires `name`;
- append-only historical migration records with a missing old operator log.

## Read-only intake

`architecture_lifecycle.py intake` ran before any service mutation. Evidence
was written outside the service root.

Result:

- exit 0;
- eight source files inventoried;
- `source_unchanged=true`;
- before and after snapshot SHA-256 both
  `0db64948b5b111276c49d7e46c413b038feb7f7b64cb9334037f0080ec02141e`;
- load, latency, availability, budget, migration window, and one failure-mode
  owner remained `UNKNOWN`;
- the legacy client performed a real GET and exited 0 with
  `{"run_id":"run-1","name":"baseline","status":"running"}`.

This proved only read-only inventory and observed compatibility, not system
readiness.

## Options and real authorization stop

The option packet presented:

- `SD-A` (recommended): keep the observed single-process SQLite topology, add
  nullable `title`, backfill from `name`, preserve v1, add v2, rehearse locally;
- `SD-B`: migrate to PostgreSQL shared schema plus tested RLS if multi-instance
  writes or database-enforced isolation become real requirements;
- a microservice split was not recommended without ownership/load/scaling
  evidence.

Option packet SHA-256:
`4cfc79c40682e5aca35cdbee85c6ffcfd0c5c19baf3dff74d50b8f661a65c9d8`.

Work stopped before mutation. The user replied `行` to the explicit request to
authorize recommended `SD-A` actions `A-001` through `A-004`. Authorization was
bound to:

- the exact option digest above;
- a disposable absolute target under `.upgrade/_e2e`;
- v1 `name` retention plus v2 `title` dual-write;
- mandatory rollback;
- authorization document SHA-256
  `92026a7f9e43c6a6d6982db4f5162c0355db892bcf1cea02f6cde2a268de9713`.

## Authorized implementation

The baseline service and database were copied byte-for-byte. Initial database
SHA-256 at source, target, and rollback backup was:
`0097c9c491fdc1f52d3b04e66bd116392c302c16f9c63125c98882ec10c89270`.

Authorized artifacts in the disposable target:

- SQLite `003_add_title.sql`: `BEGIN IMMEDIATE`, additive nullable `title`,
  backfill `title=name`, commit;
- application dual-write of `name` and `title`;
- exact v1 response shape retained; v2 exposes `title`;
- OpenAPI 3.1 contract with v1/v2 request, success, and error examples;
- ADR explaining the recommendation, alternative, and compatibility cost;
- JSON schema spec and generated Mermaid ER text;
- package manifest with evidence states and hashes.

No removal of `name` was generated or authorized.

## Database, data, compatibility, and rollback

First application:

- migration exit 0;
- baseline row became `name=baseline,title=baseline`;
- `PRAGMA integrity_check` returned `ok`;
- the legacy v1 client still exited 0;
- v1 POST and v2 POST both returned 201;
- v1 omitted `title`; v2 returned it;
- tenant-b GET returned no tenant-a rows;
- run responses contained no PII email.

Rollback:

- restored the eight baseline files from the pre-mutation backup;
- target and baseline file sets/hashes matched exactly;
- database SHA-256 returned exactly to
  `0097c9c491fdc1f52d3b04e66bd116392c302c16f9c63125c98882ec10c89270`;
- the rolled-back legacy client exited 0 and returned only the baseline row.

Reapply:

- migration, integrity, foreign-key, ER/schema, legacy, v2, contract, and
  boundary checks all exited 0;
- baseline data remained present;
- a new v2 run had identical `name`/`title`;
- missing tenant returned 400 and cross-tenant owner returned 403.

## Real defects exposed and fixed

The run exposed more than the planned happy path:

1. **Unknown collapse.** Missing intake requirement/current-state categories
   were normalized to empty arrays, falsely turning unknown into known-empty.
   The lifecycle now preserves literal `UNKNOWN`; sparse-manifest self-tests
   cover requirements, components, interfaces, and client inventory.
2. **Quoted identifier false positive.** The SQL scanner did not mask
   MySQL/SQLite backtick identifiers. A table named `` `DROP TABLE` `` could
   trigger a false destructive finding. Backticks, escaped backticks, correct
   statement lines, and an unclosed-token error are now tested.
3. **Procedural-body blind spot.** A `CREATE FUNCTION ... $body$` body was
   masked but not reported as uninspected. It now emits
   `DYNAMIC-SQL-UNINSPECTED` without pretending to parse generated SQL.
4. **Referenced response examples skipped.** Contract validation skipped
   examples behind local response `$ref`. It now resolves those references;
   the target contract validates 16 request/response/error examples.
5. **Missing tenant misclassified.** A missing `X-Tenant-ID` fell through to a
   database constraint and returned 409. The boundary now returns 400.
6. **Cross-tenant owner write.** With tenant-b present, posting as tenant-b
   with tenant-a owner `user-1` returned 201. The service now checks owner
   membership before insert and returns 403. This was an observed defect, not a
   prewritten expected result.

The last two fixes exist only in the disposable rehearsal service. They
demonstrate the workflow; they are not changes to another repository/system.

## Migration heuristic

A PostgreSQL 18/context fixture included comments and strings containing fake
DDL plus real DROP/RENAME, `CREATE INDEX CONCURRENTLY` inside a transaction,
volatile default, immediate constraint validation, `VALIDATE`, `SET NOT NULL`,
`ALTER TYPE`, and dynamic SQL.

`schema_lint.py` exited 1 with:

- 2 critical;
- 6 major;
- 2 review;
- 0 minor.

The fake comment/string DDL did not match. A MySQL backtick regression fixture
matched only the real `DROP COLUMN`; the backtick names and `ADD CONSTRAINT`
did not create spurious DROP/ADD-column results.

This exit code means only that the configured lexical heuristic matched. It is
not a SQL parser, catalog diff, lock simulator, execution plan, zero-downtime
proof, research finding, or orchestrator gate.

## OpenAPI and ER verification

System Python intentionally returned `STRUCTURE_ONLY`, exit 2, because
`openapi-spec-validator` was absent. A disposable venv then installed
`openapi-spec-validator` 0.9.0:

- target OpenAPI: `VALIDATED`, 16 examples, exit 0;
- bundled OpenAPI template: `VALIDATED`, 6 examples, exit 0.

JSON Schema checks do not prove implementation behavior, authorization,
performance, or compatibility.

`er_diagram.py --strict` generated four entities and four relationships.
SQLite catalog comparison confirmed:

- entity set equals non-internal table set;
- relationship child/parent pairs equal all database foreign keys;
- `foreign_key_check=[]`;
- `integrity_check=ok`.

`mmdc` was unavailable, so Mermaid evidence is syntax/structure only, not a
pixel rendering claim.

## Package evidence

`architecture_lifecycle.py verify-package` returned exit 0:

- `VERIFIED=4`;
- `UNAVAILABLE=2`;
- `FAILED=0`;
- package valid.

The unavailable checks were PostgreSQL/RLS execution (`psql` absent) and
Mermaid pixel rendering (`mmdc` absent). Package manifest SHA-256 was
`721c4026f7c8b69226361ec7c1e8edfde8b264182613c267a583e9ed7013f5a2`.

## Boundaries

- `system-design`: system/API/schema migration, compatibility, ADR, reliability
  and evidence package.
- `project-structure`: no project tree migration was delegated or performed.
- `data-engineering`: no research-dataset quality, lineage, split, or release
  claim was absorbed.
- `frontend-design`: no interaction/UI implementation was performed.
- `research-ethics`: PII and tenant controls became design/test items; no
  privacy or ethics clearance was declared.
- `orchestrator`: `STAGE_GATES` and `ROUTES` still have zero system-design,
  `schema_lint`, or `er_diagram` entries. No findings/stage/back-edge exists.

## Regression evidence

- all four system-design script self-tests: exit 0;
- project-structure, data-engineering, research-ethics, orchestrator, and
  frontend related self-tests: pass after required Windows UTF-8 rerun;
- one first-pass upstream issue was preserved: frontend `ai_tell_lint.py`
  raised `UnicodeEncodeError` under default GBK while printing emoji; with
  `PYTHONUTF8=1` it passed. This system-design task did not modify that skill;
- `python -m _shared`: pass;
- relevant `compileall`: pass;
- skill-creator `quick_validate`: pass;
- bundled JSON parsing, SQL lexical scan, SQL heuristic, OpenAPI validator, and
  `git diff --check`: pass.

Temporary `.upgrade/_e2e` content was deleted after this evidence was written.
