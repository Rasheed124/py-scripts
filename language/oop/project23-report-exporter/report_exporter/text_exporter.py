
class TextExporter:

    def __init__(self, file_name ):
        self.__file_name =  file_name

    @property
    def file_name(self) -> str:
        return self.__file_name


    def export(self, data):
        if not self.file_name.endswith(".txt"):
            self.file_name += ".txt"

        with open(self.file_name, "w", encoding="utf-8") as file:
            for item in data:
                for key, value in item.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")
