from collections.abc import Mapping, Sequence
from .validators import normalize_file_name

class TextExporter:
    def __init__(self, file_name: str):
        self.__file_name = normalize_file_name(file_name, "txt")

    @property
    def file_name(self) -> str:
        return str(self.__file_name)

    def export(self, data: Sequence[Mapping]) -> str:
        if not isinstance(data, (list, tuple)):
            raise TypeError("Text export data must be a list or tuple of dictionaries.")
        if not all(isinstance(row, Mapping) for row in data):
            raise TypeError("Every report row must be a dictionary-like mapping.")

        with open(self.file_name, "w", encoding="utf-8") as file:
            file.write("EMPLOYEE REPORT\n")
            file.write("=" * 40 + "\n\n")
            if not data:
                file.write("No records found.\n")
            for index, item in enumerate(data, start=1):
                file.write(f"Record {index}\n")
                for key, value in item.items():
                    file.write(f"{key.replace('_', ' ').title()}: {value}\n")
                file.write("\n")
        return self.file_name
