import shutil
import tempfile

from pathlib import Path

from vibe_firmware.utils.zip_utils import (
    extract_firmware_files,
)


class InstallService:

    def install_zip(
        self,
        zip_file: Path,
        firmware_dir: Path,
    ) -> None:

        with tempfile.TemporaryDirectory() as tmp:

            extracted = extract_firmware_files(
                zip_file,
                Path(tmp),
            )
            
            print(f"Extracted files from {zip_file} to temporary directory: {tmp}")

            for file in extracted:
                print(f"Installing file {file} to {firmware_dir}")
                shutil.copy2(
                    file,
                    firmware_dir /
                    file.name,
                )

    def clean_firmware(
        self,
        firmware_dir: Path,
    ) -> None:

        for extension in (
            ".json",
            ".wasm",
            ".aot",
        ):
            for file in firmware_dir.glob(
                f"*{extension}"
            ):
                file.unlink()
