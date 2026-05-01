---
name: local-pipeline-preflight
description: "Validate local context, Python environment, ignored outputs, and CLI readiness before changing or running the compact GFS pipeline."
---

# Local Pipeline Preflight

Use this skill before changing or running the repository locally.

## Steps

1. Read `README.md`, `AGENTS.md`, and `CLAUDE.md`.
2. Confirm `git status` and check for unexpected local output files.
3. Confirm Python is available and the virtual environment instructions still make sense.
4. Confirm the main CLI commands still exist:
   - `gfs-pipeline --help`
   - `gfs-pipeline download-72h --help`
   - `gfs-pipeline plot-maps --help`
5. Confirm `.gitignore` still excludes raw data, processed CSVs, maps, and `.env`.

## Expected Output

- summary of local readiness
- blockers before running the pipeline
- minimum commands to validate after the next change
