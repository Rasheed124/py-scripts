import json
from collections.abc import Mapping, Sequence
from .validators import normalize_file_name

class JSONExporter:
    def __init__(self, file_name: str):
        self.__file_name = normalize_file_name(file_name, "json")

    @property
    def file_name(self) -> str:
        return str(self.__file_name)

    def export(self, data: Sequence[Mapping]) -> str:
        if not isinstance(data, (list, tuple)):
            raise TypeError("JSON export data must be a list or tuple of dictionaries.")
        if not all(isinstance(row, Mapping) for row in data):
            raise TypeError("Every report row must be a dictionary-like mapping.")

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(list(data), file, indent=4, ensure_ascii=False)
        return self.file_name
