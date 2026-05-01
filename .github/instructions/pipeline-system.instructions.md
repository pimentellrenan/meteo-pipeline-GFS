---
applyTo: "src/gfs_pipeline/pipeline.py, src/gfs_pipeline/noaa.py, src/gfs_pipeline/transform.py, src/gfs_pipeline/cli.py"
---

# Pipeline System - Technical Reference

Auto-attached to changes in the compact GFS pipeline implementation.

## Pipeline Architecture

```text
NOAA NOMADS
    ->
download_72h() / download_grib()        src/gfs_pipeline/noaa.py
    ->
extract_points()                        src/gfs_pipeline/transform.py
    ->
run_pipeline() / plot_72h_maps()        src/gfs_pipeline/pipeline.py
    ->
CSV in data/processed or PNG maps in data/maps
```

## Scope Constraints

- This repository only supports NOAA GFS.
- The default portfolio window is 72 hours.
- The default forecast hours are `0, 18, 36, 54, 72`.
- Keep the pipeline local-first and easy to inspect.

## Download Rules

- Reuse an existing GRIB2 file if it already exists and is non-empty.
- Use the filtered NOMADS URL, not the full raw archive, to keep downloads compact.
- Keep retries bounded and fail with a useful message if download still fails.

## Point Extraction Rules

- Input points must provide `name`, `latitude`, and `longitude`.
- Extraction uses nearest-gridpoint selection.
- Longitude must be normalized with `% 360` before selection because GFS may expose 0-360 coordinates.

## Data Sanity Expectations

| Variable | Expected unit | Plausible range |
|---|---|---|
| `t2m` | K in raw output | roughly 200-330 |
| `tp` / `apcp` | mm or accumulated kg/m^2 | non-negative |
| surface wind speed | m/s | usually 0-60 |
| 500 hPa height | dam after conversion | usually 480-620 |

## Safety Checklist

- Before changing the download URL, verify the requested levels and variables still match the plotting layer.
- Before changing extracted variables, verify `README.md` and plotting docs still describe the same outputs.
- Before changing CLI defaults, update `README.md`, `AGENTS.md`, and `.github/instructions/default.instructions.md`.
