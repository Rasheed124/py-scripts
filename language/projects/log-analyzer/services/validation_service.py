
import re

from services.log_parser import get_log_level
from utils.date_utils import parse_and_format_date


DATE_PATTERN = re.compile(
    r"\b\d{4}-\d{2}-\d{2}\b"
    r"|\b\d{1,2}/\d{1,2}/\d{4}\b"
    r"|\b\d{1,2}-\d{1,2}-\d{4}\b"
)


def validate_logs(log_entries: list[str]) -> dict:
    """Find entries with unrecognized levels or invalid dates."""
    invalid_levels = []
    invalid_dates = []

    for number, entry in enumerate(log_entries, start=1):
        if not get_log_level(entry):
            invalid_levels.append(number)

        date_match = DATE_PATTERN.search(entry)

        if date_match and not parse_and_format_date(date_match.group()):
            invalid_dates.append(number)

    return {
        "entries_checked": len(log_entries),
        "invalid_levels": invalid_levels,
        "invalid_dates": invalid_dates,
    }


def check_missing_data(log_entries: list[str]) -> dict:
    """Find empty entries and entries without recognized levels."""
    empty_lines = []
    missing_levels = []

    for number, entry in enumerate(log_entries, start=1):
        if not entry.strip():
            empty_lines.append(number)
        elif not get_log_level(entry):
            missing_levels.append(number)

    return {
        "empty_lines": empty_lines,
        "missing_levels": missing_levels,
    }
