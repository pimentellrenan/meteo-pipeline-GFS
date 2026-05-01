from pathlib import Path
from time import sleep

import requests


GFS_BASE_URL = "https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl"


def build_gfs_url(run_date: str, cycle: str, forecast_hour: int) -> str:
    """Build a NOMADS filtered GFS URL for portfolio fields."""
    forecast = f"f{forecast_hour:03d}"
    file_name = f"gfs.t{cycle}z.pgrb2.0p25.{forecast}"
    directory = f"/gfs.{run_date}/{cycle}/atmos"
    params = {
        "file": file_name,
        "lev_10_m_above_ground": "on",
        "lev_2_m_above_ground": "on",
        "lev_500_mb": "on",
        "lev_surface": "on",
        "var_HGT": "on",
        "var_TMP": "on",
        "var_APCP": "on",
        "var_UGRD": "on",
        "var_VGRD": "on",
        "dir": directory,
    }
    query = "&".join(f"{key}={value}" for key, value in params.items())
    return f"{GFS_BASE_URL}?{query}"


def download_grib(
    run_date: str,
    cycle: str,
    forecast_hour: int,
    output_dir: Path,
    timeout_seconds: int,
    max_retries: int,
) -> Path:
    """Download a filtered GFS GRIB2 file, reusing it if already present."""
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / f"gfs_{run_date}_{cycle}_f{forecast_hour:03d}.grib2"
    if destination.exists() and destination.stat().st_size > 0:
        return destination

    url = build_gfs_url(run_date, cycle, forecast_hour)
    last_error: Exception | None = None
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, timeout=timeout_seconds)
            response.raise_for_status()
            destination.write_bytes(response.content)
            if destination.stat().st_size == 0:
                raise RuntimeError("downloaded file is empty")
            return destination
        except Exception as exc:
            last_error = exc
            if attempt < max_retries:
                sleep(2 * attempt)

    raise RuntimeError(f"failed to download GFS file from {url}") from last_error
