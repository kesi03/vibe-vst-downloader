from pathlib import Path


class RemovalService:

    EXTENSIONS = (".json", ".wasm", ".aot")

    def remove_files(
        self,
        firmware_dir: Path,
        library_file: Path,
        dry_run: bool = True,
    ) -> list[Path]:
        removed_or_selected = []

        for extension in self.EXTENSIONS:
            for file in firmware_dir.glob(f"*{extension}"):
                if file.is_file():
                    removed_or_selected.append(file)

        if library_file.is_file():
            removed_or_selected.append(library_file)

        if not dry_run:
            for file in removed_or_selected:
                file.unlink()

        return removed_or_selected

    def remove_package_files(
        self,
        firmware_dir: Path,
        package_name: str,
        dry_run: bool = True,
    ) -> list[Path]:
        removed_or_selected = []

        for extension in self.EXTENSIONS:
            file = firmware_dir / f"{package_name}{extension}"

            if file.is_file():
                removed_or_selected.append(file)

                if not dry_run:
                    file.unlink()

        return removed_or_selected
