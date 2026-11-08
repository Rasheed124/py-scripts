
from collections import Counter

from services.log_parser import get_log_level


def analyze_logs(log_entries: list[str]) -> Counter:
    """Count occurrences of each recognized log level."""
    counts = Counter()

    for entry in log_entries:
        level = get_log_level(entry)

        if level:
            counts[level] += 1

    return counts
