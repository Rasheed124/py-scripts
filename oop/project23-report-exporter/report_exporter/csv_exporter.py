

import csv

class CSVExporter:

    def __init__(self, file_name ):
        self.__file_name =  file_name


    @property
    def file_name(self) -> str:
        return self.__file_name


    def export(self, data):
        if not self.file_name.endswith(".csv"):
            self.file_name += ".csv"

        with open(self.file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)




