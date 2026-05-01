---
paths:
  - "src/gfs_pipeline/pipeline.py"
  - "src/gfs_pipeline/noaa.py"
  - "src/gfs_pipeline/transform.py"
  - "src/gfs_pipeline/cli.py"
---

# Pipeline System - Quick Reference

Full reference: `.github/instructions/pipeline-system.instructions.md`

## Defaults

- Model: NOAA GFS only
- Run window: 72h
- Default forecast hours: `0, 18, 36, 54, 72`

## Key Behaviors

- `download_72h()` should remain compact and predictable.
- `extract_points()` must require `name`, `latitude`, and `longitude`.
- Longitudes should be normalized before nearest-gridpoint lookup.
- CLI changes must be reflected in `README.md`.

## Safety Checks

- If you change downloaded variables or levels, verify plotting still works.
- If you change forecast-hour defaults, update docs and agent instructions in the same change.
