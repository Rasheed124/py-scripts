import csv
from collections.abc import Mapping, Sequence
from .validators import normalize_file_name

class CSVExporter:
    def __init__(self, file_name: str):
        self.__file_name = normalize_file_name(file_name, "csv")

    @property
    def file_name(self) -> str:
        return str(self.__file_name)

    def export(self, data: Sequence[Mapping]) -> str:
        if not isinstance(data, (list, tuple)):
            raise TypeError("CSV export data must be a list or tuple of dictionaries.")
        if not data:
            raise ValueError("Cannot export an empty CSV report.")
        if not all(isinstance(row, Mapping) for row in data):
            raise TypeError("Every report row must be a dictionary-like mapping.")

        fieldnames = list(data[0].keys())
        if any(set(row.keys()) != set(fieldnames) for row in data):
            raise ValueError("All CSV rows must contain the same fields.")

        with open(self.file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return self.file_name
