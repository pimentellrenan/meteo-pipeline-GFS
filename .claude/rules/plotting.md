---
paths:
  - "src/gfs_pipeline/plotting.py"
---

# Plotting System - Quick Reference

Full reference: `.github/instructions/meteo-plot-system.instructions.md`

## Allowed Output Surface

- `surface_wind`
- `temperature_2m`
- `geopotential_500hpa`

## Critical Rules

- Keep matplotlib on the `Agg` backend for headless runs.
- Keep the output folder structure stable under `data/maps/`.
- Keep titles explicit with date, cycle, and forecast hour.

## Review Workflow

After changing plotting behavior, regenerate one compact run and verify:

- all 15 PNGs are produced;
- the CLI remains responsive with progress messages;
- units and variable naming still match the README.
