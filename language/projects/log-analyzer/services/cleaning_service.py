
def clean_logs(log_entries: list[str]) -> list[str]:
    """Remove leading and trailing whitespace from log entries."""
    return [entry.strip() for entry in log_entries]
