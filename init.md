# init.md boot slate

timestamp_utc: 2025-10-04T00:00:00Z

startup_signal:
  repo_identity: agent-zero
  repo_purpose: run autonomous research agents on GDPa1 developability data while keeping the semantic mesh authoritative context
  complement_reference: AGENTS.md

core_context:
  - README.md
  - AGENTS.md
  - research_plans/initial_plan/plan.md
  - research_plans/initial_plan/gaps.md
  - research_plans/initial_plan/gaps_risks.md
  - competition_public/2025 AbDev Competition Overview.md
  - semantic_mesh/README.md
  - semantic_mesh/semantic/README.md
  - ontology_schema/README.md

resource_snapshot:
  workspace: /workspaces/agent-zero
  git_branch: main (expected)
  cleanliness_flag: must be clean before mutate
  runtimes_expected:
    - python 3.x (modeling + analytics)
    - git (version control)
    - make/cli tooling (per plan)
    - HF CLI login + Ginkgo submission code
  credential_surface: must be empty

scope_brief:
  mission: ship open antibody developability workflow via agents anchored to mesh
  dataset_focus: GDPa1 (246 train + 80 heldout) with folds + assay semantics baked into mesh
  key_outputs:
    - reproducible feature/model pipelines (see research_plans/initial_plan)
    - semantic_mesh ontologies + validators for contextual RAG
    - leaderboard-ready submissions meeting evaluation metrics
  essential_tools:
    - python + huggingface datasets + pandas/numpy
    - rdflib/jsonschema/bibtexparser
    - git + GitHub Actions
    - mesh query utilities (planned)
  stakeholder_roles:
    - PI: approve mesh schema, data manifest, competition scope
    - research_directors: deliver validator, populate mesh, manage submissions
    - engineering_leads: own automation, CI, feature extraction

mesh_preplan_brief:
  definition: mesh = pre-plan knowledge node for whole program, tuned for AI/bioinformatician RAG
  coverage_goals:
    - encode assays, features, ontology mappings, competition rules, pipeline steps
    - expose hashes + provenance for every artefact
    - shrink tokens, keep query richness
  current_state:
    - READMEs exist; ontology outputs, mappings, validator missing
    - competition_public now holds structured competition briefs + raw GDPa1/heldout CSVs; integrate into mesh indices
    - semantic_mesh/library catalog replaces legacy templates; keep it lean + current

competition_brief:
  host: Ginkgo Datapoints × Hugging Face (2025 AbDev)
  training_phase: GDPa1 246-ab “qualifying exam” (isotype-stratified CV mandatory)
  final_phase: 80-ab heldout “final exam” scored privately
  targets: Hydrophobicity(HIC), Polyreactivity(PR_CHO), Self-association(AC-SINS pH7.4), Thermostability(Tm2), Titer
  metrics: per-property Spearman + top-decile recall (averaged)
  deadlines: early test scoring 2025-10-13; final submission 2025-11-01
  prizes: $10k Ginkgo credits or $2k cash per property + open-source prize
  submission_requirements:
    - register on Ginkgo, obtain secret code
    - upload CV + test CSVs via HF leaderboard (schema enforced)
    - identity needed for prizes (HF handle can stay anon)

todo_stack:
  mesh_build:
    - [ONGOING] extend semantic_mesh/library catalog as artefacts mature
    - [DONE] publish read-only ontology exports (JSON-LD + Turtle) via `ontology_schema/generate_ontology.py`
    - [DONE] expand mesh_bootstrap.md into mesh_manifest.yaml with hashes + owners
    - [DONE] ship navigation index + query guide for semantic_mesh
  data_ops:
    - [TODO] document read-only GDPa1 access pathways within mesh indices
  ci_enablement:
    - [TODO] stand up semantic_mesh CI workflow (supersedes removed templates)

clarifications_needed (route to PI / research directors):
  - confirm canonical location + schema for data manifest (data/MANIFEST.yaml?)
  - assign owner + timeline for mesh validator + CI workflow
  - approve mesh population plan (ontology outputs, mappings, prompt seeds)
  - confirm registration ownership (HF usernames, Ginkgo codes) + submission cadence

ready_payload_template:
  timestamp_utc: <iso8601>
  objective_stub: <sentence>
  context_loaded:
    - path: <core_context_path>
      sha256: <hash>
  environment:
    workspace: <path>
    git_branch: <name>
    cleanliness: <clean|dirty>
  resource_status:
    python: <version_or_missing>
    git: <version_or_missing>
  open_questions: <list_or_NONE>

note: boot is read-only; behavioral execution lives in AGENTS.md post-READY.
