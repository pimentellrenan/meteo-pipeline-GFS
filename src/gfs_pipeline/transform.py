from pathlib import Path
import warnings

import cfgrib
import pandas as pd


VARIABLE_UNITS = {
    "t2m": "K",
    "tp": "mm",
    "unknown": "",
}


def load_points(points_file: Path) -> pd.DataFrame:
    points = pd.read_csv(points_file)
    required = {"name", "latitude", "longitude"}
    missing = required - set(points.columns)
    if missing:
        raise ValueError(f"points file is missing required columns: {sorted(missing)}")
    return points


def _normalize_variable_name(name: str) -> str:
    lowered = name.lower()
    if lowered in {"t2m", "2t", "tmp"} or "temperature" in lowered:
        return "t2m"
    if lowered in {"tp", "apcp"} or "precip" in lowered:
        return "tp"
    return name


def _open_datasets(grib_file: Path):
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message="In a future version of xarray the default value for compat will change",
            category=FutureWarning,
        )
        return cfgrib.open_datasets(grib_file, backend_kwargs={"indexpath": ""})


def extract_points(grib_file: Path, points_file: Path, run_date: str, cycle: str, forecast_hour: int) -> pd.DataFrame:
    """Extract nearest-gridpoint values from a GRIB2 file into a tidy table."""
    points = load_points(points_file)
    datasets = _open_datasets(grib_file)
    records: list[dict] = []

    for dataset in datasets:
        latitude_name = "latitude" if "latitude" in dataset.coords else "lat"
        longitude_name = "longitude" if "longitude" in dataset.coords else "lon"
        for raw_variable in dataset.data_vars:
            variable = _normalize_variable_name(raw_variable)
            data_array = dataset[raw_variable]
            for _, point in points.iterrows():
                selected = data_array.sel(
                    {
                        latitude_name: float(point["latitude"]),
                        longitude_name: float(point["longitude"]) % 360,
                    },
                    method="nearest",
                )
                value = float(selected.values)
                records.append(
                    {
                        "run_date": run_date,
                        "cycle": cycle,
                        "forecast_hour": forecast_hour,
                        "point_name": point["name"],
                        "latitude": float(point["latitude"]),
                        "longitude": float(point["longitude"]),
                        "variable": variable,
                        "value": value,
                        "unit": VARIABLE_UNITS.get(variable, ""),
                    }
                )

    return pd.DataFrame.from_records(records)
