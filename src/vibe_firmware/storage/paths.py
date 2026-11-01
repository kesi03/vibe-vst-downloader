from pathlib import Path
import os

APP_NAME = "VIBE FM"


class AppPaths:

    @property
    def root(self) -> Path:
        return Path(os.environ["APPDATA"]) / APP_NAME

    @property
    def downloads(self) -> Path:
        return self.root / "Downloads"

    @property
    def firmware(self) -> Path:
        return self.root / "Firmware"

    @property
    def backups(self) -> Path:
        return self.root / "Backup"

    @property
    def library(self) -> Path:
        return self.root / "library.json"

    def create(self) -> None:

        self.root.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.downloads.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.firmware.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.backups.mkdir(
            parents=True,
            exist_ok=True,
        )