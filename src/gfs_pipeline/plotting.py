from pathlib import Path

import cfgrib
import matplotlib.pyplot as plt
import numpy as np


VARIABLES = {
    "surface_wind": {
        "title": "Surface wind speed",
        "unit": "m/s",
        "cmap": "viridis",
        "file": "surface_wind",
    },
    "temperature_2m": {
        "title": "2m temperature",
        "unit": "degC",
        "cmap": "coolwarm",
        "file": "temperature_2m",
    },
    "geopotential_500hpa": {
        "title": "500 hPa geopotential height",
        "unit": "dam",
        "cmap": "plasma",
        "file": "geopotential_500hpa",
    },
}


def _open_datasets(grib_file: Path):
    return cfgrib.open_datasets(grib_file, backend_kwargs={"indexpath": ""})


def _find_variable(datasets, names: set[str], level: int | None = None):
    for dataset in datasets:
        for name in dataset.data_vars:
            if name.lower() not in names:
                continue
            if level is not None and "isobaricInhPa" in dataset.coords:
                values = dataset.coords["isobaricInhPa"].values
                if int(np.ravel(values)[0]) != level:
                    continue
            return dataset[name]
    return None


def _coords(data_array):
    lat_name = "latitude" if "latitude" in data_array.coords else "lat"
    lon_name = "longitude" if "longitude" in data_array.coords else "lon"
    return data_array[lon_name], data_array[lat_name]


def _save_field(data_array, output: Path, title: str, unit: str, cmap: str) -> Path:
    output.parent.mkdir(parents=True, exist_ok=True)
    lon, lat = _coords(data_array)

    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)
    mesh = ax.pcolormesh(lon, lat, data_array.values, shading="auto", cmap=cmap)
    colorbar = fig.colorbar(mesh, ax=ax, shrink=0.85)
    colorbar.set_label(unit)
    ax.set_title(title)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.grid(alpha=0.25)
    fig.savefig(output, dpi=140)
    plt.close(fig)
    return output


def plot_grib_maps(grib_file: Path, run_date: str, cycle: str, forecast_hour: int, output_dir: Path) -> list[Path]:
    """Plot the three portfolio variables from one GFS GRIB2 file."""
    datasets = _open_datasets(grib_file)
    created: list[Path] = []

    temperature = _find_variable(datasets, {"t2m", "2t", "tmp"})
    if temperature is not None:
        celsius = temperature - 273.15
        created.append(
            _save_field(
                celsius,
                output_dir / "temperature_2m" / f"gfs_{run_date}_{cycle}_f{forecast_hour:03d}.png",
                f"GFS 2m temperature | {run_date} {cycle}Z f{forecast_hour:03d}",
                VARIABLES["temperature_2m"]["unit"],
                VARIABLES["temperature_2m"]["cmap"],
            )
        )

    u10 = _find_variable(datasets, {"u10", "10u", "ugrd"})
    v10 = _find_variable(datasets, {"v10", "10v", "vgrd"})
    if u10 is not None and v10 is not None:
        wind_speed = np.sqrt(u10**2 + v10**2)
        created.append(
            _save_field(
                wind_speed,
                output_dir / "surface_wind" / f"gfs_{run_date}_{cycle}_f{forecast_hour:03d}.png",
                f"GFS surface wind speed | {run_date} {cycle}Z f{forecast_hour:03d}",
                VARIABLES["surface_wind"]["unit"],
                VARIABLES["surface_wind"]["cmap"],
            )
        )

    height = _find_variable(datasets, {"gh", "hgt"}, level=500)
    if height is not None:
        dam = height / 10.0
        created.append(
            _save_field(
                dam,
                output_dir / "geopotential_500hpa" / f"gfs_{run_date}_{cycle}_f{forecast_hour:03d}.png",
                f"GFS 500 hPa geopotential height | {run_date} {cycle}Z f{forecast_hour:03d}",
                VARIABLES["geopotential_500hpa"]["unit"],
                VARIABLES["geopotential_500hpa"]["cmap"],
            )
        )

    return created
