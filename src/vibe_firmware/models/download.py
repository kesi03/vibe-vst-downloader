from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class DownloadResult:
    package_id: str
    file_path: Path
