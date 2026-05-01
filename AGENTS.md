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

## Documentation Governance

- `README.md` remains the primary human-facing document.
- Agent instructions belong in `AGENTS.md`, `CLAUDE.md`, `.claude/rules/**`, `.github/instructions/**`, `.github/prompts/**`, and `.agents/skills/**`.
- Avoid creating new markdown files unless they add operational or agent value.

## Repository Hygiene

- Do not overwrite untracked files without reading them first.
- Do not use destructive commands without explicit approval.
- Before commit and push, review the diff and confirm that no local outputs or secrets slipped in.
