# system-design Round 2 competitor study

Checked 2026-07-03. Repository stars are a discovery signal, not a quality
score. Every peer below is an actual agent skill with a `SKILL.md`; tools,
methods, official documentation, and articles are deliberately separated.
Commits are pinned so the mechanisms and line anchors remain reproducible.

## Gate and ownership facts

Repository grep on 2026-07-03 confirms that `light-system-design`,
`system-design`, `schema_lint`, and `er_diagram` are absent from
`light-orchestrator/scripts/run_checkpoint.py::STAGE_GATES` and
`light-orchestrator/scripts/reroute.py::ROUTES`. The orchestrator spec lists
engineering skills as on-demand rather than research-DAG stages.

Therefore system-design remains an off-DAG engineering skill:

- no `_shared` attachment;
- no `light.findings.v1`;
- no stage, checkpoint, route, or back-edge;
- its script exit codes describe local tool results only.

## R1 — true peer agent skills

### Repository snapshot

| Repository | Stars | Pinned commit |
|---|---:|---|
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 68,710 | [`8c65303`](https://github.com/addyosmani/agent-skills/commit/8c6530305396f341b5da7201cf1f7e390fdb863f) |
| [wshobson/agents](https://github.com/wshobson/agents) | 37,469 | [`5cc2549`](https://github.com/wshobson/agents/commit/5cc2549a50fc672230efd0a0307e2fd27ffba792) |
| [aj-geddes/useful-ai-prompts](https://github.com/aj-geddes/useful-ai-prompts) | 283 | [`3f5182c`](https://github.com/aj-geddes/useful-ai-prompts/commit/3f5182cfd739fc113f4af5244a1cf342ad7f7911) |
| [seb1n/awesome-ai-agent-skills](https://github.com/seb1n/awesome-ai-agent-skills) | 117 | [`a6c8c0e`](https://github.com/seb1n/awesome-ai-agent-skills/commit/a6c8c0ef3c240faefe1b0b5cabe1567beaea60fd) |
| [simota/agent-skills](https://github.com/simota/agent-skills) | 58 | [`1cd9949`](https://github.com/simota/agent-skills/commit/1cd994967ff6321aa8e571052f8f30bdb134930b) |
| [akillness/oh-my-skills](https://github.com/akillness/oh-my-skills) | 33 | [`0cb012d`](https://github.com/akillness/oh-my-skills/commit/0cb012d5a45123b3460f69abd0c8be2ad395981e) |

Stars were read from the GitHub repository API on 2026-07-03. No claim is made
that two skills in one repository are independent implementations.

### Mechanism matrix

| True peer skill | Evidence read | Concrete mechanism | What Light borrows | Remaining gap / caution |
|---|---|---|---|---|
| addyosmani `api-and-interface-design` | [`SKILL.md` L22–37, L125–145, L284+](https://github.com/addyosmani/agent-skills/blob/8c6530305396f341b5da7201cf1f7e390fdb863f/skills/api-and-interface-design/SKILL.md#L22) | Hyrum's Law, contract-first design, additive evolution, boundary validation, explicit checklist | Treat undocumented behavior and existing consumers as compatibility evidence; prefer additive change | No executable contract validator or current-state system inventory |
| addyosmani `deprecation-and-migration` | [`SKILL.md` L67–133, L197+](https://github.com/addyosmani/agent-skills/blob/8c6530305396f341b5da7201cf1f7e390fdb863f/skills/deprecation-and-migration/SKILL.md#L67) | Replacement first, incremental consumer migration, usage measurement, Strangler/adapter/flag patterns, zero-usage removal condition | Make deprecation, compatibility window, consumer inventory, and removal evidence part of architecture work | Guidance only; its example mentions a migration checker but bundles no checker here |
| wshobson `postgresql-table-design` | [`SKILL.md` L8–25, L120–125](https://github.com/wshobson/agents/blob/5cc2549a50fc672230efd0a0307e2fd27ffba792/plugins/database-design/skills/postgresql/SKILL.md#L8) | PostgreSQL-specific data types, constraints, access-path indexing, RLS, safe-evolution reminders | Keep dialect-specific branches and target-version premises explicit | Contains overbroad guidance: L124 calls `now()` volatile, while PostgreSQL classifies it stable; confirms the need for primary-source recheck |
| wshobson `database-migration` | [`SKILL.md` L112–166, L255–329](https://github.com/wshobson/agents/blob/5cc2549a50fc672230efd0a0307e2fd27ffba792/plugins/framework-migration/skills/database-migration/SKILL.md#L112), plus `references/details.md` | ORM examples, staged rename/type conversion, transaction and checkpoint rollback patterns | Separate schema change, data backfill, compatibility, and rollback | Often says “zero downtime” without binding it to table/version/traffic evidence; Light must not inherit that wording |
| akillness `api-design` | [`SKILL.md` L62–162](https://github.com/akillness/oh-my-skills/blob/0cb012d5a45123b3460f69abd0c8be2ad395981e/.agent-skills/api-design/SKILL.md#L62), `boundary-guide.md`, `contract-review-checklist.md` | Contract framing starts with consumers, ownership, existing clients/migrations, scale patterns; produces a bounded API packet and handoffs | Use the smallest honest artifact and route implementation/testing/auth/storage outward | Does not validate OpenAPI or examples |
| akillness `database-schema-design` | [`SKILL.md` L55–143](https://github.com/akillness/oh-my-skills/blob/0cb012d5a45123b3460f69abd0c8be2ad395981e/.agent-skills/database-schema-design/SKILL.md#L55), all three reference checklists | Storage packet classification, minimum credible evidence, access patterns, ownership/lifecycle, staged rollout, rollback/stop conditions | Adopt explicit packet type, evidence minimum, query-path rationale, and route-outs | It is a storage anchor rather than a whole-system lifecycle; no executable diff/rehearsal |
| simota `atlas` | [`SKILL.md` L47–138, L172–215](https://github.com/simota/agent-skills/blob/1cd994967ff6321aa8e571052f8f30bdb134930b/atlas/SKILL.md#L47), `adr-rfc-templates.md`, `architecture-modernization-anti-patterns.md`, `module-boundary-evaluation.md` | SURVEY→PLAN→VERIFY→PRESENT, dependency/boundary evidence, alternatives, ADR/RFC, modernization, rollback, fitness functions | Add current-state dependency/boundary inventory, explicit migration/rollback, and executable verification targets | Large amounts of uncited numeric/default advice occur in the skill; borrow mechanisms, not claims or thresholds |
| simota `gateway` | [`SKILL.md` L79–139, L188–199](https://github.com/simota/agent-skills/blob/1cd994967ff6321aa8e571052f8f30bdb134930b/gateway/SKILL.md#L79), `breaking-change-detection.md`, `deprecation-policy.md`, `api-review-checklist.md`, `openapi-templates.md` | OpenAPI/GraphQL contract, realistic examples, breaking-change classification, ask-first rules, deprecation/cutover handoffs | Make consumer breakage, example validation, deprecation, and exact validator evidence first-class | Skill mixes sound mechanisms with many universal performance/default claims; each requires independent primary-source verification |
| seb1n `api-design` | [`SKILL.md` L14–30, L227–236](https://github.com/seb1n/awesome-ai-agent-skills/blob/a6c8c0ef3c240faefe1b0b5cabe1567beaea60fd/api-and-integration/api-design/SKILL.md#L14) | REST workflow, versioning, idempotency, OpenAPI and examples | Confirms these are field-common abilities, not Light differentiators | No companion validator; several one-size-fits-all REST prescriptions |
| seb1n `database-schema-design` | [`SKILL.md` L14–32, L120–127](https://github.com/seb1n/awesome-ai-agent-skills/blob/a6c8c0ef3c240faefe1b0b5cabe1567beaea60fd/database/database-schema-design/SKILL.md#L14) | Requirements→model→normalize→constraints/indexes→DDL→iterate; multi-tenant choice | Confirms normalization, ER/schema, indexing, migration, and RLS are common | Claims multi-dialect support but examples are PostgreSQL-shaped; no dialect execution evidence |
| aj-geddes `rest-api-design` | [`SKILL.md`](https://github.com/aj-geddes/useful-ai-prompts/blob/3f5182cfd739fc113f4af5244a1cf342ad7f7911/skills/rest-api-design/SKILL.md), [`validate-api.sh` L11–18](https://github.com/aj-geddes/useful-ai-prompts/blob/3f5182cfd739fc113f4af5244a1cf342ad7f7911/skills/rest-api-design/scripts/validate-api.sh#L11) | Concise REST checklist plus references/template/script surface | Negative lesson: distinguish named validation from actual validation | Script contains only TODO comments and still prints “validation complete”; Light must mark validator absence `UNAVAILABLE`, never pass |
| aj-geddes `database-migration-management` | [`SKILL.md`](https://github.com/aj-geddes/useful-ai-prompts/blob/3f5182cfd739fc113f4af5244a1cf342ad7f7911/skills/database-migration-management/SKILL.md), [`validate-schema.sh` L11–18](https://github.com/aj-geddes/useful-ai-prompts/blob/3f5182cfd739fc113f4af5244a1cf342ad7f7911/skills/database-migration-management/scripts/validate-schema.sh#L11) | Migration/versioning/rollback topic map with SQL template | Negative lesson: verified claims need command, result, locator, and hash | Validator is also a TODO that always prints success |

This is 12 true peer skills across six repositories. Clean/Hexagonal, REST,
GraphQL, gRPC, ADR, idempotency, consistency, OpenAPI, RLS,
expand/migrate/contract, schema review, and deprecation are clearly common
capabilities.

## Tools — not counted as agent skills

| Tool | Actual role | Honest routing from Light |
|---|---|---|
| [Squawk](https://squawkhq.com/) | PostgreSQL migration linter | Use when its PostgreSQL rule coverage fits; do not equate Light regexes with its parser/rules |
| [Atlas](https://atlasgo.io/) | schema-as-code, inspection, diff/migration lint/apply workflows | Use for real current↔desired diff/drift after selecting the engine |
| [Skeema](https://www.skeema.io/) | MySQL/MariaDB schema management and diff | Use for MySQL-family declarative schema workflows |
| [sqlfluff](https://docs.sqlfluff.com/) | multi-dialect SQL formatting/linting | Use for syntax/style support; it is not a migration safety proof |
| [Alembic](https://alembic.sqlalchemy.org/) | SQLAlchemy migration runner and revision graph | Preserve generated/manual revision limits and target DB tests |
| [Flyway](https://documentation.red-gate.com/flyway) | versioned/repeatable DB migrations | Use the installed edition/capability actually available |
| [Liquibase](https://docs.liquibase.com/) | changelog-based database change management | Verify dialect and rollback coverage for each change type |
| [Prisma Migrate](https://www.prisma.io/docs/orm/prisma-migrate) | Prisma schema migration workflow | Use when Prisma is the selected stack; inspect generated SQL |
| [openapi-spec-validator](https://github.com/python-openapi/openapi-spec-validator) | Python OpenAPI document validator | `contract_validate.py` reports `UNAVAILABLE` when absent |

Tool names do not satisfy the peer-skill count. Nor does pointing at a tool
prove that a Light workflow executed it.

## Methods, standards, and official documentation — not peers

| Source | Mechanism used | Limitation |
|---|---|---|
| [C4 model](https://c4model.com/) | context/container/component views | Diagrams alone do not supply contracts, migration, or evidence |
| [MADR](https://adr.github.io/madr/) | tradeoff-explicit ADR structure | ADR presence does not prove a decision was tested |
| [Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html) | incremental modernization | Not automatically safer; needs boundary, routing, data, fallback, and exit evidence |
| [OpenAPI 3.2.0](https://spec.openapis.org/oas/latest.html) | current published HTTP API description standard | Project tooling may rationally select an earlier supported minor |
| [PostgreSQL 11 release notes](https://www.postgresql.org/docs/11/release-11.html) | constant-default no-rewrite introduction | Function volatility, target major, locks, table size, and runner context still matter |
| [PostgreSQL 18 ALTER TABLE](https://www.postgresql.org/docs/18/sql-altertable.html) | lock levels, `NOT VALID`, validation, `SET NOT NULL` behavior | Does not predict workload impact without the target system |
| [PostgreSQL 18 CREATE INDEX](https://www.postgresql.org/docs/18/sql-createindex.html) | concurrent index behavior and transaction restriction | Concurrent builds have extra work and failure caveats |
| [PostgreSQL RLS](https://www.postgresql.org/docs/18/ddl-rowsecurity.html) | default-deny and bypass behavior | Security/performance require actual-role tests |
| [SQLite ALTER TABLE](https://sqlite.org/lang_altertable.html) | SQLite-specific supported changes and generalized rebuild procedure | PostgreSQL rules do not transfer |

No gRPC “5–10×” performance claim or RLS millisecond claim is retained. Such
numbers require a workload, hardware, versions, configuration, dataset, and
reproducible benchmark.

## Old-claim audit

| Old claim | Round 2 verdict |
|---|---|
| No peer combines layers, API, data flow, migration lint, artifacts, online lookup, and decision points | Withdrawn as an uniqueness claim. It was a broad conjunction, while peers already cover most mechanisms in overlapping packets. |
| Clean/Hexagonal, REST/GraphQL/gRPC, ADR, idempotency, consistency, OpenAPI, RLS, expand-contract, schema lint are special | False as differentiation; these are common field capabilities. |
| Squawk/Atlas/Skeema/sqlfluff/Alembic/Flyway/Liquibase/Prisma prove peer coverage | Category error; they are tools, not peer agent skills. |
| `schema_lint.py` can determine migration safety | Withdrawn. It is a lexical/regex heuristic with explicit dialect/version/context premises. |
| `schema.sql`, `openapi.yaml`, and `rls_policy.sql` are generally ready to use | Withdrawn. They are now labeled examples with dialect/version/assumption limits. |
| Critical/major exit 1 is a system or research gate | False. It means only that this local heuristic matched configured rules. |
| RLS file presence proves tenant isolation | False. Runtime roles, bypass behavior, session context, policies, queries, and tests determine the result. |

## R2 mechanism adopted in Light

Light's defensible contribution is narrower than the old “everything in one
skill” story. It is a repository-specific, tested lifecycle that:

1. freezes a read-only existing-system source inventory before option design;
2. preserves requirement/current-state unknowns instead of filling them;
3. requires recommendation + viable alternative + rejection/exit conditions;
4. stops for a real user selection before selected artifacts or mutations;
5. binds disposable mutations to option digest and action IDs;
6. separates schema review, real diff/drift, SQL heuristic, execution rehearsal,
   compatibility, and rollback;
7. refuses to call YAML parsing OpenAPI validation;
8. permits `VERIFIED` only with command/cwd/return code/locator/hash/timestamp;
9. keeps system-design off-DAG and routes scientific data, UI, and ethics
   judgments to their owners.

Several peers cover individual parts of this list. The claim is not global
novelty; the claim to test is that this exact local lifecycle and its evidence
mechanics work end to end.

## R3 package binding supplement

Checked 2026-07-05. A later review found a remaining gap after the option
digest and authorization work: `verify-package` could validate local artifact
hashes and `VERIFIED` logs without proving that the package belonged to the
selected authorization, implemented only approved action IDs, or preserved the
read-only intake snapshot for an existing system.

The adopted mechanism is package-level binding: `package-manifest.json` must
include `authorization_binding` with a package-local authorization file
locator/SHA-256, option ID, option-packet SHA-256, and approved action IDs;
`implemented_action_ids` must be a subset of those approved actions; each
verification entry must bind to implemented action IDs; and existing-system
packages must bind `intake-integrity.json` by locator/SHA-256/source snapshot.
This does not prove the architecture is optimal. It only prevents a package
from using unrelated artifacts or logs to masquerade as the authorized design.

## Access tiers

| Tier | Resources | Role |
|---|---|---|
| Local free | Python stdlib, SQLite, scripts/templates, installed DB/validator tools | Core intake/evidence path |
| Public free | pinned GitHub source, PostgreSQL/SQLite/OpenAPI docs | R1 and version-sensitive verification |
| Free login/key | higher API limits, hosted registries | Optional |
| Institution/cloud restricted | private source, staging DB, telemetry | Optional project evidence |
| Paid/closed | commercial schema/architecture platforms | Never a core dependency |

## Evidence notes

- Peer repositories were shallow-cloned to a temporary directory, pinned at the
  commits above, and their named SKILL/reference/script files were read.
- GitHub API star counts and official documentation were checked 2026-07-03.
- Temporary research clones are not part of the repository or delivery.
- This file is research evidence, not a live version database. Recheck
  version-sensitive claims when applying them.
