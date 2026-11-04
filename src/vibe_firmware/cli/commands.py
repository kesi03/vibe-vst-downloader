from __future__ import annotations

import argparse

from vibe_firmware.constants import DOWNLOAD_BASE_URL
from vibe_firmware.storage.paths import AppPaths
from vibe_firmware.utils.http import HttpClient
from vibe_firmware.storage.file_repository import FileRepository
from vibe_firmware.services.library_service import LibraryService
from vibe_firmware.services.download_service import DownloadService
from vibe_firmware.services.install_service import InstallService
from vibe_firmware.services.backup_service import BackupService
from vibe_firmware.services.removal_service import RemovalService
from vibe_firmware.services.firmware_service import FirmwareService
from vibe_firmware.services.synch_service import SyncService


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="vibe-fw",
        description="VIBE FM Firmware Manager",
    )

    parser.add_argument(
        "command",
        choices=[
            "download",
            "install",
            "force",
            "sync",
            "remove",
        ],
    )

    parser.add_argument(
        "--package",
        help="Remove only this package's matching files",
    )

    args = parser.parse_args()

    #
    # Shared services
    #

    paths = AppPaths()
    paths.create()

    http = HttpClient()

    repository = FileRepository()

    library_service = LibraryService(http)

    download_service = DownloadService(
        http,
        DOWNLOAD_BASE_URL,
    )

    install_service = InstallService()

    backup_service = BackupService()

    removal_service = RemovalService()

    firmware_service = FirmwareService(
        paths=paths,
        libraries=library_service,
        downloads=download_service,
        installs=install_service,
        backups=backup_service,
    )

    sync_service = SyncService(
        paths=paths,
        library_service=library_service,
        download_service=download_service,
        install_service=install_service,
        backup_service=backup_service,
        repository=repository,
    )

    #
    # Commands
    #

    if args.command == "download":
        firmware_service.download_all()

    elif args.command == "install":
        firmware_service.install_all()

    elif args.command == "force":
        firmware_service.force_download_install()

    elif args.command == "sync":
        sync_service.sync()

    elif args.command == "remove":

        if args.package:
            files = removal_service.remove_package_files(
                paths.firmware,
                args.package,
                dry_run=False,
            )
        else:
            files = removal_service.remove_files(
                paths.firmware,
                paths.library,
                dry_run=False,
            )

        for file in files:
            print(f"Removed: {file}")

        if not files:
            print("No matching files found.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
