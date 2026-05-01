---
name: plot-review
description: "Review a compact GFS map-generation change for correctness, output stability, and local reproducibility."
---

# Plot Review

Use this skill when reviewing a change to `src/gfs_pipeline/plotting.py`.

## Checks

- plotting still uses the `Agg` backend
- output paths remain stable under `data/maps/`
- the three supported plot families are unchanged unless intentionally expanded
- the CLI still reports progress during long plot runs
- local runs do not require a GUI session

## Expected Result

- findings by severity
- residual local reproduction risks
- the smallest useful follow-up validation command
