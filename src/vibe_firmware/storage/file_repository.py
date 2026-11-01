
import json
from pathlib import Path
from typing import Any


class FileRepository:

    @staticmethod
    def load_json(path: Path) -> Any:

        if not path.exists():
            return None

        return json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )

    @staticmethod
    def save_json(
        path: Path,
        value: Any,
    ) -> None:

        path.write_text(
            json.dumps(
                value,
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
