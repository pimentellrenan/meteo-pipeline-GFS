# GFS Weather Pipeline - Essential AI Instructions

## Available Prompts

| Prompt | File | When to use |
|---|---|---|
| `/fix-plot` | `.github/prompts/fix-plot.prompt.md` | A map looks wrong, blank, clipped, or physically implausible |
| `/debug-pipeline` | `.github/prompts/debug-pipeline.prompt.md` | A download, extraction, or forecast CSV looks suspicious |

## Context-Attached Instructions

| Edited path | Loaded instruction |
|---|---|
| `src/gfs_pipeline/plotting.py` | `meteo-plot-system.instructions.md` |
| `src/gfs_pipeline/pipeline.py`, `src/gfs_pipeline/noaa.py`, `src/gfs_pipeline/transform.py` | `pipeline-system.instructions.md` |

## Scope

This repository implements:

- a compact NOAA GFS pipeline;
- local GRIB2 download and caching;
- nearest-point extraction into CSV;
- small-scope map generation for three variables;
- a cross-agent repository layout for Claude Code, Codex, and GitHub Copilot.

## Source of Truth

- `README.md` is the human-facing source of truth.
- For commands, local reproduction, and repository purpose, read `README.md` first.
- Use code as the final reference when documentation and implementation diverge.

## Technical Flow

- Download: `src/gfs_pipeline/noaa.py`
- Point extraction: `src/gfs_pipeline/transform.py`
- Orchestration: `src/gfs_pipeline/pipeline.py`
- Plotting: `src/gfs_pipeline/plotting.py`
- CLI: `src/gfs_pipeline/cli.py`

## Key Commands

- Help: `gfs-pipeline --help`
- Download short run: `gfs-pipeline download-72h --date YYYYMMDD --cycle 00`
- Plot maps: `gfs-pipeline plot-maps --date YYYYMMDD --cycle 00`
- Extract one CSV: `gfs-pipeline run --date YYYYMMDD --cycle 00 --forecast-hour 18`

## Change Rules

- Do not create extra markdown files for small implementation changes.
- Keep repository knowledge centralized in `README.md` and the agent instruction files.
- Whenever CLI behavior changes, update `README.md` in the same change.
- Whenever the agent workflow changes, update `AGENTS.md`, `CLAUDE.md`, or the relevant instruction file in the same change.
