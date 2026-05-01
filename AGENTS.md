# gfs-weather-pipeline - AGENTS.md

These instructions apply to any agent working in this repository.

## Required Reading

- `README.md`
- `CLAUDE.md`
- `.github/instructions/default.instructions.md`
- `.github/instructions/pipeline-system.instructions.md`
- `.github/instructions/meteo-plot-system.instructions.md`
- `.claude/rules/doc-sync.md`
- `.claude/rules/pipeline.md`
- `.claude/rules/plotting.md`

## Tool-to-File Matrix

This matrix is explicit on purpose: use it to decide which context files to read before making changes.

| File or path | Read by tool or workflow | Why it is read |
|---|---|---|
| `README.md` | Any agent, any human reviewer | Source of truth for scope, commands, and local workflow |
| `AGENTS.md` | Any agent | Shared repository contract and delivery rules |
| `CLAUDE.md` | Claude Code, agents aligning with Claude workflow | Claude-facing shortcuts and context mapping |
| `.github/copilot-instructions.md` | GitHub Copilot | Copilot-facing repository constraints |
| `.github/instructions/default.instructions.md` | Agents changing repo-wide behavior, GitHub-aware tooling | Default AI instructions for this repository |
| `.github/instructions/pipeline-system.instructions.md` | Agents changing `src/gfs_pipeline/cli.py`, `src/gfs_pipeline/pipeline.py`, `src/gfs_pipeline/noaa.py`, `src/gfs_pipeline/transform.py` | Pipeline architecture, invariants, and safety checklist |
| `.github/instructions/meteo-plot-system.instructions.md` | Agents changing `src/gfs_pipeline/plotting.py` | Plotting invariants, output scope, and review checklist |
| `.claude/rules/doc-sync.md` | Agents making code or workflow changes | Documentation sync requirements |
| `.claude/rules/pipeline.md` | Agents touching pipeline code | Condensed pipeline rules |
| `.claude/rules/plotting.md` | Agents touching plotting code | Condensed plotting rules |
| `.github/prompts/debug-pipeline.prompt.md` | `/debug-pipeline` workflow | Reusable debugging prompt for pipeline issues |
| `.github/prompts/fix-plot.prompt.md` | `/fix-plot` workflow | Reusable debugging prompt for plotting issues |
| `.agents/skills/local-pipeline-preflight/SKILL.md` | `local-pipeline-preflight` skill | Preflight checks before running or changing the pipeline |
| `.agents/skills/plot-review/SKILL.md` | `plot-review` skill | Review workflow for map-generation changes |

## Repository Identity

- Product: compact NOAA GFS ETL and plotting pipeline for local execution.
- Scope: one short 72h run, point extraction, and a small plotting surface.
- Runtime: local Python CLI and optional Docker.
- Primary command group: `gfs-pipeline`.
- Supported plots: surface wind speed, 2m temperature, and 500 hPa geopotential height.

## Current Scope

- Pipeline code in `src/gfs_pipeline`.
- Configuration in `config`.
- Human-facing docs in `README.md`.
- Agent-facing guidance in `AGENTS.md`, `CLAUDE.md`, `.claude/rules/**`, `.github/instructions/**`, `.github/prompts/**`, and `.agents/skills/**`.
- Output artifacts must stay local under `data/`.

## Local-First Policy

- This repository intentionally does not include CI/CD workflows.
- Do not add GitHub Actions unless the project goal changes explicitly.
- Do not introduce cloud deployment, managed secrets, or production infrastructure here.
- Keep the repo easy to reproduce on a laptop with Python or Docker.

## Safety Rules

- Never commit credentials, tokens, service-account files, or `.env`.
- Never commit downloaded GRIB2 files, generated CSVs, or generated PNG maps.
- Before changing CLI behavior, update `README.md` in the same work.
- Before changing plotting behavior, update the plotting instructions if the rule set changes.

## Delivery Flow

1. Read the required files before changing the pipeline or plotting behavior.
2. Keep code changes narrow and aligned with the local portfolio scope.
3. Update human docs and agent docs in the same change when behavior changes.
4. Validate the CLI locally before commit.

## Real Task Examples

Use these examples as the default workflow unless the user requests something narrower.

### If asked to alter CLI behavior

Read:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/instructions/default.instructions.md`
- `.github/instructions/pipeline-system.instructions.md`
- `.claude/rules/doc-sync.md`

Then validate with:

- `gfs-pipeline --help`
- `gfs-pipeline download-72h --help`
- `gfs-pipeline plot-maps --help`

Also update in the same change:

- `README.md`
- this `AGENTS.md` file if the operating contract changed

### If asked to alter pipeline download or extraction logic

Read:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/instructions/pipeline-system.instructions.md`
- `.claude/rules/pipeline.md`
- `.claude/rules/doc-sync.md`

Then validate with:

- `gfs-pipeline download-72h --help`
- `gfs-pipeline run --help`

### If asked to alter plotting behavior

Read:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/instructions/meteo-plot-system.instructions.md`
- `.claude/rules/plotting.md`
- `.agents/skills/plot-review/SKILL.md`

Then validate with:

- `gfs-pipeline plot-maps --help`

If local data is already available, prefer one compact end-to-end check:

- `gfs-pipeline plot-maps --date 20260501 --cycle 00`

## Documentation Governance

- `README.md` remains the primary human-facing document.
- Agent instructions belong in `AGENTS.md`, `CLAUDE.md`, `.claude/rules/**`, `.github/instructions/**`, `.github/prompts/**`, and `.agents/skills/**`.
- Avoid creating new markdown files unless they add operational or agent value.

## Repository Hygiene

- Do not overwrite untracked files without reading them first.
- Do not use destructive commands without explicit approval.
- Before commit and push, review the diff and confirm that no local outputs or secrets slipped in.
