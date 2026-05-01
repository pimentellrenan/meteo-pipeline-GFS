from pathlib import Path

from .config import settings
from .noaa import download_grib
from .plotting import plot_grib_maps
from .transform import extract_points


DEFAULT_FORECAST_HOURS = [0, 18, 36, 54, 72]


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


def download_72h(
    run_date: str,
    cycle: str,
    forecast_hours: list[int] | None = None,
    progress_callback=None,
) -> list[Path]:
    """Download the compact 72h GFS portfolio set."""
    hours = forecast_hours or DEFAULT_FORECAST_HOURS
    downloaded: list[Path] = []
    for hour in hours:
        if progress_callback is not None:
            progress_callback(f"Downloading forecast hour f{hour:03d}")
        downloaded.append(
            download_grib(
                run_date=run_date,
                cycle=cycle,
                forecast_hour=hour,
                output_dir=settings.data_dir,
                timeout_seconds=settings.timeout_seconds,
                max_retries=settings.max_retries,
            )
        )
    return downloaded


def plot_72h_maps(
    run_date: str,
    cycle: str,
    forecast_hours: list[int] | None = None,
    output_dir: Path | None = None,
    progress_callback=None,
) -> list[Path]:
    """Plot five figures for each portfolio variable."""
    hours = forecast_hours or DEFAULT_FORECAST_HOURS
    plot_dir = output_dir or settings.map_dir
    created: list[Path] = []
    for hour in hours:
        if progress_callback is not None:
            progress_callback(f"Plotting forecast hour f{hour:03d}")
        grib_file = settings.data_dir / f"gfs_{run_date}_{cycle}_f{hour:03d}.grib2"
        if not grib_file.exists():
            raise FileNotFoundError(f"GRIB2 file not found: {grib_file}")
        created.extend(plot_grib_maps(grib_file, run_date, cycle, hour, plot_dir))
    return created
