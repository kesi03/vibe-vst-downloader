import shutil
import zipfile
from pathlib import Path


ALLOWED_EXTENSIONS = {
    ".json",
    ".wasm",
    ".aot",
}


def extract_firmware_files(
    archive_path: Path,
    target_directory: Path,
) -> list[Path]:
    extracted: list[Path] = []

    target_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    with zipfile.ZipFile(archive_path) as archive:
        for member in archive.infolist():
            if member.is_dir():
                continue

            filename = Path(member.filename).name

            if Path(filename).suffix.lower() not in ALLOWED_EXTENSIONS:
                continue

            target = target_directory / filename

            with archive.open(member) as src:
                with target.open("wb") as dst:
                    shutil.copyfileobj(src, dst)

            extracted.append(target)

    return extracted
