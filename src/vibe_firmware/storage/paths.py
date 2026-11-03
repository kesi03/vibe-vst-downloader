from pathlib import Path
import platform
import os

APP_NAME = "VIBE FM"


class AppPaths:
    @property
    def root(self) -> Path:
        system = platform.system()

        if system == "Windows":
            return Path(os.environ["APPDATA"]) / APP_NAME

        if system == "Darwin":  # macOS
            return (
                Path.home()
                / "Library"
                / "Application Support"
                / APP_NAME
            )

        if system == "Linux":
            return (
                Path.home()
                / ".local"
                / "share"
                / APP_NAME
            )

        raise RuntimeError(f"Unsupported operating system: {system}")

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
        self.root.mkdir(parents=True, exist_ok=True)
        self.downloads.mkdir(parents=True, exist_ok=True)
        self.firmware.mkdir(parents=True, exist_ok=True)
        self.backups.mkdir(parents=True, exist_ok=True)
