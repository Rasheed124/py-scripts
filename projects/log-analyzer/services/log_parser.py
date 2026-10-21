
import re


LOG_LEVEL_PATTERN = re.compile(
    r"\b(INFO|WARNING|ERROR|DEBUG|CRITICAL)\b",
    re.IGNORECASE,
)


def get_log_level(line: str) -> str | None:
    """Extract a recognized log level from a log entry."""
    match = LOG_LEVEL_PATTERN.search(line)

    return match.group(1).upper() if match else None
