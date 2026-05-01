# Documentation Sync Rules

When changing code in this repository, update the corresponding human and agent documentation in the same change.

## Mapping Table

| When you change... | Update these files |
|---|---|
| `src/gfs_pipeline/cli.py` | `README.md`, `AGENTS.md`, `.github/instructions/default.instructions.md` |
| `src/gfs_pipeline/pipeline.py` | `README.md`, `AGENTS.md`, `.github/instructions/pipeline-system.instructions.md` |
| `src/gfs_pipeline/noaa.py` | `README.md` when download behavior changes, `.github/instructions/pipeline-system.instructions.md` |
| `src/gfs_pipeline/transform.py` | `.github/instructions/pipeline-system.instructions.md`, `.claude/rules/pipeline.md` |
| `src/gfs_pipeline/plotting.py` | `README.md` when outputs change, `.github/instructions/meteo-plot-system.instructions.md`, `.claude/rules/plotting.md` |
| `Dockerfile` | `README.md`, `AGENTS.md` |
| `.github/prompts/**` or `.agents/skills/**` | `README.md` and `AGENTS.md` if the agent workflow changes materially |

## Verification

After updating documentation, verify:

- `README.md` still matches the real CLI flow
- `AGENTS.md` still describes the current scope
- the instruction files still match the actual repository layout
