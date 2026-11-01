from dataclasses import dataclass

@dataclass(slots=True)
class FirmwarePackage:
    id: str
    name: str
    version: str
    file_url: str