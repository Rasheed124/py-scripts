import json
from pathlib import Path
from typing import Any
from .base import Storage




class LocalStorage(Storage):
    """Store each JSON-compatible record in its own file."""

    def __init__(self, directory: str | Path | None = None) -> None:
        if directory is None:
            directory = Path(__file__).parent.parent / "data"

        self._directory = Path(directory)
        self._directory.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _validate_key(key: str) -> None:
        if not isinstance(key, str):
            raise TypeError("Storage key must be a string.")
        if not key.strip():
            raise ValueError("Storage key cannot be empty.")
        if key in {".", ".."} or "/" in key or "\\" in key:
            raise ValueError("Storage key cannot contain path separators.")

    def _path_for(self, key: str) -> Path:
        self._validate_key(key)
        return self._directory / f"{key}.json"

    def save(self, key: str, data: Any) -> None:
        path = self._path_for(key)
        try:
            with path.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except (TypeError, ValueError) as error:
            raise ValueError("Data must be JSON-serializable for LocalStorage.") from error

    def get(self, key: str) -> Any:
        path = self._path_for(key)
        if not path.is_file():
            raise KeyError(f"No record found for key: {key!r}")
        try:
            with path.open("r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError as error:
            raise ValueError(f"Stored record {key!r} contains invalid JSON.") from error

    def delete(self, key: str) -> None:
        path = self._path_for(key)
        try:
            path.unlink()
        except FileNotFoundError:
            raise KeyError(f"No record found for key: {key!r}") from None
