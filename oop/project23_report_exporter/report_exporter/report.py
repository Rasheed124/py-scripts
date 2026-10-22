from collections.abc import Sequence

def generate_report(data, exporter) -> str:
    """Export data through any object with a callable export(data) method."""
    export_method = getattr(exporter, "export", None)
    if not callable(export_method):
        raise TypeError(
            "Invalid exporter: expected an object with a callable export(data) method."
        )
    return export_method(data)

def generate_reports(data, exporters: Sequence) -> list[str]:
    """Run the same report workflow for multiple exporters."""
    return [generate_report(data, exporter) for exporter in exporters]
