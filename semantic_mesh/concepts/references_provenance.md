# References and Provenance Sources

updated_utc: 2025-10-05T13:21:00Z  
sources: `semantic_mesh/REFERENCES.md`, `semantic_mesh/library/catalog.yaml`, `competition_public/2025 AbDev Competition Overview.md`

## Citation Registry
- Primary ledger: `semantic_mesh/REFERENCES.md` (append-only, chronological updates).
- Each mesh node must reference at least one citation ID; maintain backlinks in `mesh_manifest.yaml`.

## Provenance Tracking
- Dataset hashes stored in `library/catalog.yaml` (add `sha256` field upon computation).
- Feature generation scripts record Git commit, environment manifest, and dataset version.

## Governance Rules
- New external sources require license review; document status in `research_plans/initial_plan/gaps_risks.md`.
- When deprecating a source, mark it as `retired` but leave citation for historical traceability.

## Reporting
- Publish quarterly provenance report summarizing new citations, updated hashes, and outstanding approvals.
- Use `reports/provenance/YYYY-MM-summary.md` template (to be created) for consistency.
