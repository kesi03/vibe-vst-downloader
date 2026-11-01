from datetime import datetime
from pathlib import Path
import shutil


class BackupService:

    def create_backup(
        self,
        firmware_dir: Path,
        backup_root: Path,
    ) -> Path:

        backup_dir = (
            backup_root /
            datetime.now().strftime(
                "%Y%m%d-%H%M%S"
            )
        )

        backup_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        for extension in (
            ".json",
            ".wasm",
            ".aot",
        ):

            for file in firmware_dir.glob(
                f"*{extension}"
            ):

                shutil.copy2(
                    file,
                    backup_dir / file.name,
                )

        return backup_dir

    def create_package_backup(
        self,
        firmware_dir: Path,
        backup_root: Path,
        package_name: str,
    ) -> Path:

        backup_dir = (
            backup_root /
            datetime.now().strftime(
                "%Y%m%d-%H%M%S"
            )
        )

        backup_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        for extension in (
            ".json",
            ".wasm",
            ".aot",
        ):

            source = (
                firmware_dir /
                f"{package_name}{extension}"
            )

            if source.exists():

                shutil.copy2(
                    source,
                    backup_dir /
                    source.name,
                )

        return backup_dir