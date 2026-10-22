from report_exporter import CSVExporter, JSONExporter, TextExporter, XMLExporter
from report_exporter.report import generate_report, generate_reports

data = [
    {"name": "John", "department": "Engineering", "salary": 300000},
    {"name": "Mary", "department": "Marketing", "salary": 250000},
    {"name": "David", "department": "Design", "salary": 280000},
]

def main() -> None:
    exporters = [
        CSVExporter("employee"),
        JSONExporter("employee"),
        TextExporter("employee"),
        XMLExporter("employee"),
    ]

    print("=== EXPORTING EMPLOYEE REPORTS ===")
    for result in generate_reports(data, exporters):
        print(f"Created: {result}")

    print("\n=== INVALID EXPORTER TEST ===")

    class InvalidExporter:
        def display(self):
            return "I cannot export reports."

    try:
        generate_report(data, InvalidExporter())
    except TypeError as error:
        print(f"Invalid exporter rejected: {error}")

if __name__ == "__main__":
    main()
