from __future__ import annotations

from vibe_firmware.models import (
    FirmwarePackage,
)

from vibe_firmware.services.library_service import (
    LibraryService,
)

from vibe_firmware.services.download_service import (
    DownloadService,
)

from vibe_firmware.services.install_service import (
    InstallService,
)

from vibe_firmware.services.backup_service import (
    BackupService,
)

from vibe_firmware.storage.paths import (
    AppPaths,
)

from vibe_firmware.storage.file_repository import (
    FileRepository,
)


class SyncService:

    def __init__(
        self,
        paths: AppPaths,
        library_service: LibraryService,
        download_service: DownloadService,
        install_service: InstallService,
        backup_service: BackupService,
        repository: FileRepository,
    ) -> None:

        self.paths = paths
        self.library_service = library_service
        self.download_service = download_service
        self.install_service = install_service
        self.backup_service = backup_service
        self.repository = repository

    def sync(
        self,
    ) -> None:

        library = (
            self.library_service
            .get_library()
        )

        local_library = (
            self.repository.load_json(
                self.paths.library
            )
            or {}
        )

        #
        # Support:
        #
        # [
        #   {...}
        # ]
        #
        # or:
        #
        # {
        #   "ok": true,
        #   "library": [...]
        # }
        #

        if isinstance(
            local_library,
            dict,
        ):

            local_entries = (
                local_library.get(
                    "library",
                    [],
                )
            )

        else:

            local_entries = (
                local_library
            )

        local_versions: dict[
            str,
            str,
        ] = {}

        for item in local_entries:

            if not isinstance(
                item,
                dict,
            ):
                continue

            local_versions[
                str(item["id"])
            ] = str(
                item.get(
                    "version",
                    "",
                )
            )

        updates: list[
            tuple[
                FirmwarePackage,
                str,
            ]
        ] = []

        for package in (
            library.packages
        ):

            installed_version = (
                local_versions.get(
                    package.id,
                    "",
                )
            )

            if (
                installed_version
                != package.version
            ):

                updates.append(
                    (
                        package,
                        installed_version,
                    )
                )

        if not updates:

            print(
                "No updates available."
            )

            return

        print()

        print(
            f"Found {len(updates)} update(s)"
        )

        print()

        for index, (
            package,
            installed_version,
        ) in enumerate(
            updates,
            start=1,
        ):

            print(
                f"[{index}] "
                f"{package.name} "
                f"Installed: "
                f"{installed_version or 'not installed'} "
                f"Available: "
                f"{package.version}"
            )

        print()

        print(
            "[a] Download and install all"
        )

        print(
            "[s] Select updates"
        )

        print(
            "[q] Quit"
        )

        print()

        choice = input(
            "Choice: "
        ).strip().lower()

        if choice == "q":

            print(
                "Cancelled."
            )

            return

        if choice == "a":

            selected = [
                package
                for package, _
                in updates
            ]

        elif choice == "s":

            selection = input(
                "Enter package numbers "
                "(example: 1,3,5): "
            ).strip()

            try:

                indexes = {
                    int(
                        value.strip()
                    )
                    for value in
                    selection.split(",")
                    if value.strip()
                }

            except ValueError:

                print(
                    "Invalid selection."
                )

                return

            selected = [
                package
                for index,
                (
                    package,
                    _,
                )
                in enumerate(
                    updates,
                    start=1,
                )
                if index in indexes
            ]

        else:

            print(
                "Cancelled."
            )

            return

        if not selected:

            print(
                "Nothing selected."
            )

            return

        print()

        total = len(
            selected
        )

        for current, package in enumerate(
            selected,
            start=1,
        ):

            print(
                f"[{current}/{total}] "
                f"{package.name} "
                f"{package.version}"
            )

            #
            # Backup only the package
            # being updated
            #

            self.backup_service.create_package_backup(
                self.paths.firmware,
                self.paths.backups,
                package.id,
            )

            #
            # Download package
            #

            zip_file = (
                self.download_service.download(
                    package,
                    self.paths.downloads,
                )
            )

            #
            # Install package
            #

            self.install_service.install_zip(
                zip_file,
                self.paths.firmware,
            )

        #
        # Save latest library
        #

        self.repository.save_json(
            self.paths.library,
            {
                "ok": True,
                "library": [
                    {
                        "id": package.id,
                        "name": package.name,
                        "version": package.version,
                        "file": package.file_url,
                    }
                    for package in
                    library.packages
                ],
            },
        )

        print()

        print(
            "Synchronisation completed."
        )