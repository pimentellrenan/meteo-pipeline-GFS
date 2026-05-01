# GFS Weather Pipeline

A compact portfolio project that demonstrates an end-to-end meteorological data pipeline for the **NOAA Global Forecast System (GFS)**.

The pipeline downloads GFS GRIB2 files, extracts weather values for monitored locations, and writes a tidy CSV dataset that can be loaded into a database, dashboard, or API.

![Pipeline overview](docs/assets/pipeline-overview.svg)

## What It Shows

- NOAA GFS URL construction and forecast-cycle selection.
- GRIB2 download with retries and local caching.
- Point extraction from gridded meteorological data.
- A reproducible CLI workflow.
- A small Docker image for local runs.
- Clean repository structure suitable for portfolio review.

## Repository Layout

```text
src/gfs_pipeline/
  cli.py          Command-line interface
  config.py       Environment and runtime settings
  noaa.py         GFS URL building and file download
  transform.py    GRIB-to-point transformation
  pipeline.py     End-to-end orchestration
config/
  points.csv      Example monitored locations
examples/
  sample_forecast.csv
docs/assets/
  pipeline-overview.svg
```

## Quick Start

Install locally:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

Run a small GFS extraction:

```bash
gfs-pipeline run --date 20260501 --cycle 00 --forecast-hour 6
```

The output is written to:

```text
data/processed/gfs_points_<date>_<cycle>_f<forecast_hour>.csv
```

## Docker

```bash
docker build -t gfs-pipeline .
docker run --rm -v "%cd%/data:/app/data" gfs-pipeline run --date 20260501 --cycle 00 --forecast-hour 6
```

On Linux/macOS:

```bash
docker run --rm -v "$PWD/data:/app/data" gfs-pipeline run --date 20260501 --cycle 00 --forecast-hour 6
```

## CLI Options

```bash
gfs-pipeline run \
  --date 20260501 \
  --cycle 00 \
  --forecast-hour 6 \
  --points config/points.csv \
  --output-dir data/processed
```

Key options:

- `--date`: GFS run date in `YYYYMMDD`.
- `--cycle`: forecast cycle, one of `00`, `06`, `12`, `18`.
- `--forecast-hour`: forecast horizon, for example `0`, `6`, `24`, `72`.
- `--points`: CSV with `name`, `latitude`, and `longitude`.
- `--no-download`: reuse a previously downloaded GRIB2 file.

## Example Output

```csv
run_date,cycle,forecast_hour,point_name,latitude,longitude,variable,value,unit
20260501,00,6,Sao Paulo,-23.55,-46.63,t2m,292.1,K
20260501,00,6,Sao Paulo,-23.55,-46.63,tp,0.8,mm
```

See [examples/sample_forecast.csv](examples/sample_forecast.csv).

## Notes

This is a portfolio-friendly version of a larger operational meteorological ingestion system. It keeps the public repository focused on one reproducible model, one clear pipeline, and a small amount of code that is easy to inspect.
