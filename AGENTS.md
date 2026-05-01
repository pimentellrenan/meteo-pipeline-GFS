# Agent Operating Guide

This repository is intentionally prepared for AI-assisted development across Claude Code, Codex, and GitHub Copilot.

## Project Scope

- Keep the project local-first and portfolio-friendly.
- The pipeline should only target NOAA GFS.
- The default operational window is 72 hours.
- Plot only these portfolio map products:
  - surface wind speed
  - 2m temperature
  - 500 hPa geopotential height
- Generate five figures per variable by default: `f000`, `f018`, `f036`, `f054`, `f072`.
- Treat the repository as a template for other agent-assisted projects, not just a weather demo.

## Guardrails

- Do not add CI/CD workflows. This repo demonstrates local execution and agent-ready structure.
- Do not commit downloaded GRIB2 files, generated PNG maps, `.env`, or local data outputs.
- Keep the code small and readable. Prefer explicit functions over framework-heavy abstractions.
- When adding new tasks, create a new prompt or rule instead of expanding an unrelated one.
- Update `README.md` whenever CLI behavior, generated outputs, or agent instructions change.

## Validation

Before publishing changes, run:

```bash
python -m py_compile src/gfs_pipeline/*.py
gfs-pipeline --help
gfs-pipeline download-72h --help
gfs-pipeline plot-maps --help
```
