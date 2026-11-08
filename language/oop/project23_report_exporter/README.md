# Problem 23 — Duck-Typed Report Exporter

A modular Python project demonstrating duck typing with CSV, JSON, plain-text, and XML exporters.

## Structure

    project23_report_exporter/
    ├── main.py
    └── report_exporter/
        ├── __init__.py
        ├── validators.py
        ├── report.py
        ├── csv_exporter.py
        ├── json_exporter.py
        ├── text_exporter.py
        └── xml_exporter.py

## Run

From this project directory, run:

    python main.py

It creates employee.csv, employee.json, employee.txt, and employee.xml in the current working directory.

## Concepts

- Exporter classes do not inherit from a shared parent class.
- Each exporter provides a compatible export(data) method.
- generate_report() does not check concrete exporter types.
- XMLExporter requires no change to generate_report().
- Invalid exporters are rejected with a clear TypeError.
- Filename extensions are normalized in the constructor, not assigned through a read-only property.
