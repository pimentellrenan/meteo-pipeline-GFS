from pathlib import Path

from .config import settings
from .noaa import download_grib
from .transform import extract_points


def run_pipeline(
    run_date: str,
    cycle: str,
    forecast_hour: int,
    points_file: Path | None = None,
    output_dir: Path | None = None,
    download: bool = True,
) -> Path:
    """Run the compact GFS pipeline and return the generated CSV path."""
    points_path = points_file or settings.points_file
    output_path = output_dir or settings.output_dir
    output_path.mkdir(parents=True, exist_ok=True)

    grib_file = settings.data_dir / f"gfs_{run_date}_{cycle}_f{forecast_hour:03d}.grib2"
    if download:
        grib_file = download_grib(
            run_date=run_date,
            cycle=cycle,
            forecast_hour=forecast_hour,
            output_dir=settings.data_dir,
            timeout_seconds=settings.timeout_seconds,
            max_retries=settings.max_retries,
        )

    if not grib_file.exists():
        raise FileNotFoundError(f"GRIB2 file not found: {grib_file}")

    frame = extract_points(grib_file, points_path, run_date, cycle, forecast_hour)
    destination = output_path / f"gfs_points_{run_date}_{cycle}_f{forecast_hour:03d}.csv"
    frame.to_csv(destination, index=False)
    return destination
