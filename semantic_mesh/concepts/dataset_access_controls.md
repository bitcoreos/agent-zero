# Dataset Access Controls

sources: `competition_public/GDPa1 Dataset Overview.md`, `competition_public/dataset/README.md`, `AGENTS.md`

## Access Workflow
- Require explicit acceptance of the GDPa1 dataset license before anyone receives file paths.
- Authenticate via `huggingface-cli login` using scoped tokens stored in the secrets vault; never embed tokens in scripts.

## Handling Rules
- Treat `competition_public/dataset/*` as immutable; any mutation triggers the critical error escalation defined in `competition_public/dataset/README.md`.
- Mount datasets read-only in compute environments; enforce filesystem ACLs prohibiting write operations.

## Audit & Provenance
- Log SHA256 hashes, file sizes, and retrieval timestamps to `data/audit/gdpa1_manifest.json`.
- Re-verify hashes before every training or submission run; abort if any mismatch occurs.

## Secret Hygiene
- Rotate Hugging Face tokens quarterly or after suspected compromise.
- Scrub tokens from logs/stdout; add automated scans to CI to prevent accidental leakage.

## Incident Response
- If corruption is detected, freeze modeling runs, notify the project maintainer, and restore from clean artefact cache.
- Document resolution steps and link to the governance incident register for future audits.

## Related Mesh Topics
- `semantic_mesh/concepts/bioinformatics_pipeline.md`
- `semantic_mesh/concepts/governance` (see `AGENTS.md`)
- `semantic_mesh/concepts/submission_automation.md`
