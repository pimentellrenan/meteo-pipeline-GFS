@AGENTS.md

# Claude Code Instructions

## Rules

- After modifying CLI commands, verify the CLI sections in `README.md` and `AGENTS.md`.
- After modifying plotting behavior, verify `.github/instructions/meteo-plot-system.instructions.md`.
- After modifying download, extraction, or point-processing behavior, verify `.github/instructions/pipeline-system.instructions.md`.

## Self-Updating Documentation

When making structural changes, always check `.claude/rules/doc-sync.md` to keep human docs and agent docs aligned in the same change.

### Key Mappings

- New CLI command -> update `README.md`, `AGENTS.md`, `.github/instructions/default.instructions.md`
- Pipeline behavior change -> verify `.github/instructions/pipeline-system.instructions.md`
- Plotting behavior change -> verify `.github/instructions/meteo-plot-system.instructions.md`
- New directory under `src/` -> update `README.md` and `AGENTS.md`

## Available Slash-Style Prompts

| Command | File | Purpose |
|---|---|---|
| `/debug-pipeline` | `.github/prompts/debug-pipeline.prompt.md` | Diagnose a broken or suspicious GFS data run |
| `/fix-plot` | `.github/prompts/fix-plot.prompt.md` | Diagnose and correct map-generation issues |

## Context Files

| Path pattern | Loaded file | Content |
|---|---|---|
| `src/gfs_pipeline/plotting.py` | `.github/instructions/meteo-plot-system.instructions.md` | Plotting rules, invariants, and review workflow |
| `src/gfs_pipeline/pipeline.py`, `src/gfs_pipeline/noaa.py`, `src/gfs_pipeline/transform.py` | `.github/instructions/pipeline-system.instructions.md` | Download, extraction, and sanity rules |
| `src/gfs_pipeline/plotting.py` | `.claude/rules/plotting.md` | Condensed plotting rules |
| `src/gfs_pipeline/pipeline.py`, `src/gfs_pipeline/noaa.py`, `src/gfs_pipeline/transform.py` | `.claude/rules/pipeline.md` | Condensed pipeline rules |

## Environment

- Windows development with PowerShell is supported.
- A local virtual environment is expected for Python runs.
- PowerShell activation: `.venv\Scripts\activate`.
- bash/zsh activation: `source .venv/bin/activate`.
