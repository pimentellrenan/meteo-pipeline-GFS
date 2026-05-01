---
applyTo: "src/gfs_pipeline/plotting.py"
---

# Plotting System - Technical Reference

Auto-attached to changes in the GFS plotting code.

## Plotting Scope

Only these plots belong in this repository:

- surface wind speed
- 2m temperature
- 500 hPa geopotential height

The default portfolio output is five figures per variable: `f000`, `f018`, `f036`, `f054`, `f072`.

## Architecture

```text
GRIB2 file
    ->
plot_grib_maps()             src/gfs_pipeline/plotting.py
    ->
_find_variable()
    ->
_save_field()
    ->
data/maps/<variable>/gfs_<date>_<cycle>_fNNN.png
```

## Critical Rules

- Use a non-interactive matplotlib backend (`Agg`) for local automation and Docker compatibility.
- Keep output paths stable by variable folder.
- Keep titles explicit about run date, cycle, and forecast hour.
- Avoid adding cartographic dependencies unless they materially improve the repository goal.

## Variable Handling

| Output | Raw fields |
|---|---|
| `temperature_2m` | `t2m`, `2t`, `tmp` |
| `surface_wind` | `u10`, `10u`, `ugrd` plus `v10`, `10v`, `vgrd` |
| `geopotential_500hpa` | `gh`, `hgt` at 500 hPa |

## Review Checklist

- Confirm all 15 PNG files are created for a successful 72h plot run.
- Confirm no GUI backend or display dependency is required.
- Confirm plot titles and units still match the data transformations.
