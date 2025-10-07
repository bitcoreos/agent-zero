# Semantic Mesh Bootstrap

version: 0.1.0
created_utc: 2025-10-04T00:00:00Z
status: pre-plan (declarative)

## Mesh Mission (human layer)
- compress every antibody-developability knowledge element needed to win the AbDev competition into queryable, low-token surfaces
- align competition intelligence (competition_public) with execution intent (research_plans/initial_plan)
- provide deterministic hooks for future validators, RAG agents, and human reviewers

## Knowledge Domains
| domain_id | description | canonical artefacts | key concepts |
|-----------|-------------|---------------------|--------------|
| antibody_fundamentals | structural & biophysical context for antibodies | `semantic_mesh/schemas/glossary.md`, GDPa1 documentation | VH/VL chains, CDR regions, assays (HIC, PR_CHO, AC-SINS, Tm2, Titer) |
| dataset_intel | GDPa1 + heldout sequence packaging | `competition_public/GDPa1 Dataset Overview.md`, `competition_public/dataset/*` | schema fields, gating, folds, accession provenance |
| competition_meta | rules & evaluation framing | `competition_public/2025 AbDev Competition Overview.md`, `AbDev Leaderboard Overview.md` | cross-validation protocol, deadlines, submission schema |
| modeling_strategy | internal plan to produce predictions | `research_plans/initial_plan/plan.md`, `gaps.md`, `gaps_risks.md`, `flow.md` | feature stacks (ANARCI, Markov, PBT, LMs), curriculum, ensembles |
| governance_controls | risk & compliance scaffolding | `AGENTS.md`, `init.md`, `gaps_risks.md` | orchestration policy, validation gates, licensing checkpoints |

## JSON-LD Frame (machine layer)
```json
{
  "@context": {
    "mesh": "urn:mesh:",
    "doc": "urn:doc:",
    "concept": "mesh:Concept",
    "artifact": "mesh:Artifact",
    "covers": {"@id": "mesh:covers", "@type": "@id"},
    "source": {"@id": "mesh:source", "@type": "@id"},
    "tag": {"@id": "mesh:tag"}
  },
  "@graph": [
    {
      "@id": "mesh:AntibodyFundamentals",
      "@type": "concept",
      "tag": ["antibody", "biophysics"],
      "covers": [
  "doc:semantic_mesh/schemas/glossary.md",
        "doc:competition_public/GDPa1 Dataset Overview.md"
      ]
    },
    {
      "@id": "mesh:DatasetIntel",
      "@type": "concept",
      "tag": ["dataset", "schema"],
      "covers": [
        "doc:competition_public/dataset/GDPa1_v1.2_sequences.csv",
        "doc:competition_public/dataset/heldout-set-sequences.csv"
      ]
    },
    {
      "@id": "mesh:ModelingStrategy",
      "@type": "concept",
      "tag": ["modeling", "pipeline"],
      "covers": [
        "doc:research_plans/initial_plan/plan.md",
        "doc:research_plans/initial_plan/gaps.md",
        "doc:research_plans/initial_plan/flow.md"
      ]
    }
  ]
}
```

## Mesh Nodes (YAML excerpt)
```yaml
nodes:
  - id: antibody_fundamentals
    level: base
    summary: "Defines structural antibody vocabulary (VH/VL, CDRs, assays)"
    artifacts:
      - path: competition_public/GDPa1 Dataset Overview.md
  - path: semantic_mesh/schemas/glossary.md
    queries:
      - "what is AC-SINS_pH7.4 and why does it matter?"
      - "list GDPa1 assay columns with units"
  - id: dataset_assets
    level: base
    summary: "Sequences and schema for GDPa1 + heldout"
    artifacts:
      - path: competition_public/dataset/GDPa1_v1.2_sequences.csv
      - path: competition_public/dataset/README.md
      - path: competition_public/dataset/heldout-set-sequences.csv
  - id: modeling_playbook
    level: applied
    summary: "Feature and model architecture to produce leaderboard submissions"
    artifacts:
      - path: research_plans/initial_plan/plan.md
      - path: research_plans/initial_plan/gaps.md
      - path: research_plans/initial_plan/gaps_risks.md
    key_features:
      - ANARCI region features
      - Markov + surprisal curriculum
      - Pattern-based tests (PBT)
      - LM-based multi-task head
```
```

## Pre-Execution Action Stack
1. **Index expansion**: propagate `mesh_manifest.yaml` referencing nodes above with hashes + owners.
2. **Ontology materialization**: ✅ maintained via `ontology_schema/generate_ontology.py` writing Turtle/JSON-LD exports under `ontology_schema/`.
3. **Navigation surfacing**: publish read-only navigation index + query guide for the mesh.
4. **Mesh integrity checklist**: keep provenance hashes + owners current inside `mesh_manifest.yaml`.

## Clarification Hooks
- confirm canonical namespace (`https://agent-zero.ai/mesh#`) or supply alternative before minting IDs
- confirm owners for each node (PI vs research director vs engineering lead)
- confirm whether competition_public artefacts should be clipped/summarized before ingestion to reduce token budgets

## Ready Signals
- agent should not mutate resources; mesh remains read-only with provenance tracked via hashes
- once navigation + ontology exports land, integrate references into CI per `init.md` todo_stack

```note
Declarative only: no external installations, no directives—just schema stubs so agents can reason over antibodies, assays, datasets, and our modeling plan.
```
