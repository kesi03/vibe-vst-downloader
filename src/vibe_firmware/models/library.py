from dataclasses import dataclass

from vibe_firmware.models.firmware import FirmwarePackage

@dataclass(slots=True)
class FirmwareLibrary:
    packages: list[FirmwarePackage]