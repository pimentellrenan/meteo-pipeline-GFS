from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    data_dir: Path = Path(os.getenv("GFS_DATA_DIR", "data/raw"))
    output_dir: Path = Path(os.getenv("GFS_OUTPUT_DIR", "data/processed"))
    points_file: Path = Path(os.getenv("GFS_POINTS_FILE", "config/points.csv"))
    timeout_seconds: int = int(os.getenv("GFS_TIMEOUT_SECONDS", "120"))
    max_retries: int = int(os.getenv("GFS_MAX_RETRIES", "3"))


settings = Settings()
