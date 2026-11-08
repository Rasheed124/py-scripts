import xml.etree.ElementTree as ET
from collections.abc import Mapping, Sequence
from .validators import normalize_file_name

class XMLExporter:
    """An extra exporter added without changing generate_report()."""
    def __init__(self, file_name: str):
        self.__file_name = normalize_file_name(file_name, "xml")

    @property
    def file_name(self) -> str:
        return str(self.__file_name)

    def export(self, data: Sequence[Mapping]) -> str:
        if not isinstance(data, (list, tuple)):
            raise TypeError("XML export data must be a list or tuple of dictionaries.")
        if not all(isinstance(row, Mapping) for row in data):
            raise TypeError("Every report row must be a dictionary-like mapping.")

        root = ET.Element("report")
        for row in data:
            record = ET.SubElement(root, "record")
            for key, value in row.items():
                field = ET.SubElement(record, str(key))
                field.text = str(value)

        tree = ET.ElementTree(root)
        ET.indent(tree, space="    ")
        tree.write(self.file_name, encoding="utf-8", xml_declaration=True)
        return self.file_name
