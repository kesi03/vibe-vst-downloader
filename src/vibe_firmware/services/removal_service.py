from pathlib import Path


class RemovalService:
    EXTENSIONS = (".json", ".wasm", ".aot")

    # Package names that should never be removed
    PROTECTED_PACKAGES = {
        "obervave-fm1",
    }

    def _is_protected(self, file: Path) -> bool:
        """
        Returns True if the file belongs to a protected package.
        Examples:
            obervave-fm1.json
            obervave-fm1.wasm
            obervave-fm1.aot
        """
        return file.stem in self.PROTECTED_PACKAGES

    def remove_files(
        self,
        firmware_dir: Path,
        library_file: Path,
        dry_run: bool = False,
    ) -> list[Path]:
        removed_or_selected = []

        for extension in self.EXTENSIONS:
            for file in firmware_dir.glob(f"*{extension}"):
                if not file.is_file():
                    continue

                if self._is_protected(file):
                    continue

                removed_or_selected.append(file)

        if (
            library_file.is_file()
            and not self._is_protected(library_file)
        ):
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
        # Never remove protected packages
        if package_name in self.PROTECTED_PACKAGES:
            return []

        removed_or_selected = []

        for extension in self.EXTENSIONS:
            file = firmware_dir / f"{package_name}{extension}"

            if file.is_file():
                removed_or_selected.append(file)

                if not dry_run:
                    file.unlink()

        return removed_or_selected
