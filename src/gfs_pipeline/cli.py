from pathlib import Path

import click

from .pipeline import run_pipeline


@click.group()
def cli() -> None:
    """NOAA GFS weather pipeline."""


@cli.command()
@click.option("--date", "run_date", required=True, help="GFS run date in YYYYMMDD format.")
@click.option("--cycle", required=True, type=click.Choice(["00", "06", "12", "18"]), help="GFS cycle.")
@click.option("--forecast-hour", required=True, type=int, help="Forecast horizon, for example 6 or 24.")
@click.option("--points", "points_file", type=click.Path(exists=True, path_type=Path), default=None)
@click.option("--output-dir", type=click.Path(file_okay=False, path_type=Path), default=None)
@click.option("--download/--no-download", default=True, help="Download from NOAA or reuse a local GRIB2 file.")
def run(
    run_date: str,
    cycle: str,
    forecast_hour: int,
    points_file: Path | None,
    output_dir: Path | None,
    download: bool,
) -> None:
    """Download a GFS file and extract point forecasts."""
    destination = run_pipeline(
        run_date=run_date,
        cycle=cycle,
        forecast_hour=forecast_hour,
        points_file=points_file,
        output_dir=output_dir,
        download=download,
    )
    click.echo(f"Wrote {destination}")
