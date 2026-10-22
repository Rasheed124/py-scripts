

import json

class JSONExporter:

    def __init__(self, file_name ):
        self.__file_name =  file_name


    @property
    def file_name(self) -> str:
        return self.__file_name

    def export(self,data):
        if not self.file_name.endswith(".json"):
            self.file_name += ".json"

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
