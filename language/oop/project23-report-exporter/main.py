#  Duck-Typed Report Exporter


from report_exporter import CSVExporter , JSONExporter , TextExporter

def main() -> None:

    csv_exporter =  CSVExporter('employee' )
    json_exporter =  JSONExporter('employee' )
    text_exporter =  JSONExporter('employee' )

    exporter = [csv_exporter, json_exporter, text_exporter]
    for export in exporter:
        generate_report(data, export )
    
data = [
    {"name": "John", "department": "Engineering", "salary": 300000},
    {"name": "Mary", "department": "Marketing", "salary": 250000},
    {"name": "David", "department": "Design", "salary": 280000},
]


def generate_report(data, exporter):
    return exporter.export(data)


if __name__ == "__main__":
    main()