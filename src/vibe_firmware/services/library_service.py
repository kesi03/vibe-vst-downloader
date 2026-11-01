from vibe_firmware.models import (
    FirmwareLibrary,
    FirmwarePackage,
)

from vibe_firmware.utils.http import (
    HttpClient,
)

LIBRARY_URL = (
    "https://thefirmwarehub.com/api/convert/library"
)


class LibraryService:

    def __init__(
        self,
        http: HttpClient,
    ) -> None:

        self.http = http

    def get_library(
        self,
    ) -> FirmwareLibrary:

        import json

        data = self.http.get_bytes(
            LIBRARY_URL
        )

        payload = json.loads(data)

        entries = payload.get(
            "library",
            [],
        )

        packages = [
            FirmwarePackage(
                id=str(entry["id"]),
                name=str(
                    entry.get(
                        "name",
                        entry["id"],
                    )
                ),
                version=str(
                    entry.get(
                        "version",
                        "",
                    )
                ),
                file_url=str(
                    entry["file"]
                ),
            )
            for entry in entries
        ]

        return FirmwareLibrary(
            packages=packages
        )
