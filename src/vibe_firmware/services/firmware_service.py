from vibe_firmware.services.download_service import DownloadService
from vibe_firmware.services.install_service import InstallService
from vibe_firmware.services.library_service import LibraryService
from vibe_firmware.services.backup_service import BackupService
from vibe_firmware.storage.paths import AppPaths


class FirmwareService:

    def __init__(
        self,
        paths: AppPaths,
        libraries: LibraryService,
        downloads: DownloadService,
        installs: InstallService,
        backups: BackupService,
    ) -> None:

        self.paths = paths
        self.libraries = libraries
        self.downloads = downloads
        self.installs = installs
        self.backups = backups

    def download_all(
        self,
    ) -> None:

        library = (
            self.libraries.get_library()
        )

        total = len(library.packages)

        print(
                f"Found {total} package(s)"
        )
        
        for current, package in enumerate(
                library.packages,
                start=1,
        ):
        
                print(
                    f"[{current}/{total}] "
                    f"{package.name} "
                    f"({package.version})"
                )
        
                self.downloads.download(
                    package,
                    self.paths.downloads,
                )
    def install_all(
        self,
    ) -> None:

        for zip_file in (
            self.paths.downloads.glob(
                "*.zip"
            )
        ):

            self.installs.install_zip(
                zip_file,
                self.paths.firmware,
            )

    def force_download_install(
        self,
    ) -> None:

        self.download_all()

        self.backups.create_backup(
            self.paths.firmware,
            self.paths.backups,
        )

        self.installs.clean_firmware(
            self.paths.firmware,
        )

        self.install_all()
