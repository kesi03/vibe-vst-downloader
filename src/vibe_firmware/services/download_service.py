from pathlib import Path

from vibe_firmware.models import (
    FirmwarePackage,
)

from vibe_firmware.utils.http import (
    HttpClient,
)


class DownloadService:

    def __init__(
        self,
        http: HttpClient,
        base_url: str,
    ) -> None:

        self.http = http
        self.base_url = base_url

    def download(
        self,
        package: FirmwarePackage,
        destination: Path,
    ) -> Path:

        destination.mkdir(
            parents=True,
            exist_ok=True,
        )

        zip_path = (
            destination /
            f"{package.name}-{package.version}.zip"
        )

        url = (
            self.base_url +
            "/" +
            package.file_url.lstrip("/")
        )

        

        zip_path.write_bytes(
            self.http.get_bytes(url)
        )

        return zip_path

