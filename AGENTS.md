# AGENTS.md

## Priority and Scope

* Orchestrate first. Route tasks to the right agents and surfaces. Plan before any research. Research before any execution. Execution is critical and must pass validation gates.
* Scope is repository-local. If a file is not present in this repo, it does not exist. Do not assume hidden context.
* Mixed signals are errors. Resolve conflicts before acting.

## Pre-Thinking (input processing)

* State the objective in one sentence.
* Name constraints, budgets, and non-goals.
* List explicit unknowns.
* Choose the smallest meaningful next move that reduces uncertainty.
* Draft one success metric and one stop rule.

## Orchestration and Routing

* Assign a single owner for each artifact and decision.
* Route by capability, not title. Prefer agents with the narrowest fit.
* Set budgets for time, tokens, memory, and external calls. Refuse over-budget steps unless the PI approves.
* Collapse duplicate work. Reuse prior artifacts when equivalent.

## Planning Discipline

* Define inputs, outputs, constraints, and acceptance criteria for the next unit of work.
* Declare risks and mitigation. Include a rollback plan.
* Prefer parallelizable micro-tasks with clear boundaries and locks.
* Plan to validate every intermediate artifact before it feeds downstream steps.

## Research Protocol

* Query only after planning confirms need and scope.
* Prefer low-cost evidence first. Escalate depth only when required to answer the active question.
* Record provenance, extraction schema, and caveats. Separate fact from interpretation.
* Freeze summaries for reuse. Update only with material deltas.

## Execution Protocol

* Execute the smallest unit that fulfills the current acceptance criteria.
* Keep changes reversible. Use branches, checkpoints, and clear diffs.
* Block on any failed validation gate. Revert and report.

## Validation Gates

* Input sanity: objective, data, and constraints match the plan.
* Method fit: method choice matches question and data shape.
* Metric integrity: calculations are correct and reproducible.
* Reproducibility: a peer can repeat steps from the log alone.
* Diff hygiene: minimal surface area, deliberate changes, rollback documented.

## Reasoning Protocol

* Decide with evidence tables, not intuition. Rank claims by strength and note counter-evidence.
* Articulate assumptions. Mark confidence explicitly.
* Prefer falsification tests that could prove you wrong.
* If two paths tie, pick the cheaper reversible path.

## Organization and Artifact Hygiene

* Maintain a live objective brief, study plan, evidence matrix, findings summary, and audit log.
* Version every artifact. Keep owners current. Lock finalized versions.
* Use delta updates. If nothing changed, write “no change.”

## Risk Controls

* Repo-local reality only. Do not reference unseen local files or private paths.
* Leakage: forbid any training or tuning on evaluation or submit sets.
* Licensing and policy: block on uncertainty. Do not proceed without clearance.
* Secrets: never log or store credentials. Abort if detected.
* Drift: flag when submit-set stats deviate from train-set baselines beyond thresholds.

## Communication Rules

* Lead with a task-tied acknowledgement and the current decision.
* Ask at least one clarifying question even if seemingly redundant. Provide a default path if unanswered.
* Avoid filler and meta talk. Short, precise sentences.

## Code-Writing Directives

* Design first. Pre-plan before code. Senior engineers spend months on data models and years operating and evolving deployed code.
* Contract first: define inputs, outputs, error modes, time and memory budgets, and side effects before implementation.
* Guard → Do → Verify: validate inputs, perform minimal work, assert invariants before returning.
* Composition over inheritance: small, pure units; side effects at boundaries only.
* Determinism where possible: stable ordering, fixed seeds, explicit randomness handling.
* Limits (within reason) everywhere: timeouts, bounded retries with jitter, rate limits, and backpressure.
* Observability: structured logs with correlation IDs; no secrets; minimal PII.
* Testing focus: behavior, boundaries, and one failure mode; fast and deterministic; mocks at edges.
* Size and clarity: keep modules small; single responsibility; clear docblocks explaining Why/What/How.
* Reversibility: feature flags or kill-switches for risky paths; clear rollback steps.
* Parity: keep CLI and any UI surfaces functionally equivalent; every toggle available on every surface.
* Sandboxing: Assume the AGENT is operating in a limited and delicated environment. Understand the documentation before acting.

## Task Tracking and Logging

* One intent per work item. Link each action to objective and acceptance criteria.
* Log only deltas, decisions, evidence references, costs, and failures.
* Capture start/stop times, budgets vs. actuals, and outcome status.
* Tag risks discovered, their severity, and chosen mitigations.

## Checklists

**Kickoff readiness**

* Objective, metric, scope, non-goals, budgets, risks, stop rule confirmed.
* Owner assigned; locks defined; artifacts initialized.

**Before planning locks**

* Pre-thinking complete; smallest next move chosen; validation gates defined.
* Routing decided; rollback prepared.

**Before research**

* Need confirmed by plan; evidence targets prioritized; extraction schema set.
* Cost caps set; escalation criteria written.

**Before execution**

* Inputs validated; method fit confirmed; acceptance criteria fixed.
* Rollback steps documented; observability in place.

**Before handoff**

* Findings prioritized; evidence matrix attached; open risks listed.
* Next step, owner, and budget set; costs reported vs. plan.

**Before publish**

* All validation gates pass; independent repro pass; language precise.
* Artifacts versioned and locked.

## Clarifying Questions (always ask, even if redundant)

* What is the exact objective and single success metric for this cycle?
* What is explicitly out of scope?
* What are the hard budgets for time, tokens, memory, and external calls?
* What artifact must exist at the end of this cycle and who owns it?
* What is the rollback plan if the next step fails validation?

Replacing that section with concrete signals and actions.

---

## Gaps — detection and immediate action

* Success metric baseline absent → Signal: objective brief lacks metric or threshold → Action: define metric, set baseline from last stable run, add stop rule.
* Ownership unclear → Signal: artifact without named owner and escalation path → Action: assign owner now, record backup owner.
* Rollback undefined → Signal: plan has no revert steps or checkpoints → Action: write rollback, add checkpoint, dry-run revert.
* Data split leakage risk → Signal: shared IDs between train and eval or submit set → Action: enforce unique-ID checks, block on collision.
* Cost accounting missing → Signal: no time/token/compute ledger for the cycle → Action: open a budget line, log actuals per step, abort on breach.
* Reproducibility weak → Signal: seed/config/env versions not captured → Action: freeze seeds, snapshot configs and versions, attach to log.
* Drift blind → Signal: no baseline stats for train vs submit → Action: capture train distribution, compare submit, alert on threshold exceed.
* Licensing unknown → Signal: tool/model/dataset lacks recorded license and allowed use → Action: block adoption, obtain clearance, log terms.
* Secrets unsafe → Signal: credentials visible in code, logs, or config → Action: rotate keys, scrub history, add secret scan to gates.
* Scope creep → Signal: work item not mapped to objective or non-goal list → Action: halt, request PI confirmation, re-scope.
* Validation hole → Signal: artifact without mapped gate (input/method/metric/repro/diff) → Action: add gate, re-run step.
* Routing misfit → Signal: agent executing outside capability constraints → Action: reroute to a narrower-fit agent, note rationale.
* Deadline fuzzy → Signal: no timebox or date on the cycle → Action: set hard end date and review checkpoint.
* Evidence thin → Signal: claim lacks source, counterevidence, or rating → Action: source it, rate strength, or mark “unknown.”
* Audit trail incomplete → Signal: missing deltas, decisions, or costs in the log → Action: append missing entries, lock the record.
* Dataset/version skew → Signal: artifact cites dataset without hash/date → Action: pin version+checksum, record fetch date, block stale mixes.
* Schema drift → Signal: fields added/removed without contract update → Action: lock schema, add compatibility check, fail on unexpected fields.
* Naming mismatch → Signal: columns/entities differ from canonical names → Action: map or rename to canon, add linter to enforce.
* Hidden defaults → Signal: config omits required keys but runs via implicit defaults → Action: make defaults explicit, validate presence, refuse implicit runs.
* Non-determinism → Signal: results change across runs with same inputs → Action: fix seeds, freeze RNG/time sources, serialize concurrency.
* Concurrency/locking → Signal: overlapping writes to same artifact → Action: add locks/leases, serialize critical sections, fail on contention.
* Dependency drift → Signal: unpinned libraries or tools → Action: pin versions, record SBOM, add update window with tests.
* Performance SLOs absent → Signal: no latency/memory targets per step → Action: set budgets, measure, fail on breach.
* Cache invalidation → Signal: stale outputs reused after upstream change → Action: hash inputs in cache key, purge on upstream diff.
* Long-run health → Signal: tasks without heartbeat or progress marks → Action: add heartbeats, timeouts, resumable checkpoints.
* Backup/DR → Signal: no snapshot of critical artifacts → Action: periodic backups, restore drill, document RPO/RTO.
* Access control → Signal: agents share broad write permissions → Action: least privilege, per-artifact ACLs, audit writes.
* Privacy/redaction → Signal: logs contain sensitive user or partner data → Action: redact at source, sampling, access logs to audit.
* Retry policy undefined → Signal: same handler retries arbitrarily → Action: classify retryable vs fatal, cap attempts with jittered backoff.
* Injection safety → Signal: untrusted inputs flow into prompts/tools → Action: sanitize/escape, constrain tool schemas, add allowlists.
* Time/zone drift → Signal: timestamps inconsistent across agents → Action: UTC everywhere, sync clocks, record timezone.
* Numeric stability → Signal: NaNs/inf or catastrophic cancellation in metrics → Action: add guards, epsilon thresholds, stable algorithms.
* Data imbalance → Signal: skewed label/target distributions unaddressed → Action: stratified splits, weighting, report per-slice metrics.
* Experiment registry → Signal: metrics not linked to artifacts/configs → Action: attach run ID to code/data/params, store lineage.
* Feature-flag registry → Signal: unknown flags or orphaned toggles → Action: central registry, owners, expiry dates, cleanup rule.
* Deprecation policy → Signal: legacy artifacts linger without status → Action: mark deprecated, set removal date, migration note.
* Decision escalation → Signal: blocking choice lacks approver path → Action: define escalation ladder, record approvals.
* Work-queue saturation → Signal: backlog grows without rate control → Action: cap concurrency, prioritize, shed load on pressure.
* Agent disagreement → Signal: conflicting outputs on same objective → Action: run adjudication protocol, pick tie-breaker rule, log rationale.

## Stop Conditions

* Budget exhausted without PI override.
* Any validation gate failure.
* Ruleset policy, license, or safety uncertainty.
* Evidence conflict that invalidates the plan.

## Living Document Rule

* Edits must raise signal, cut waste, or reduce risk. Optimize mixed language to ullify non-signals and increase high quality information fidelity and density. Execution is essential and must meet the same rigor as planning and research.
