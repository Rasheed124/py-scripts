
from datetime import datetime

from config import MISSING_VALUES


DATE_FORMATS = (
    "%Y-%m-%d",
    "%m/%d/%Y",
    "%d/%m/%Y",
    "%Y/%m/%d",
    "%d-%m-%Y",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%dT%H:%M:%S",
)


def parse_and_format_date(date_str: str) -> str:
    """Return a normalized YYYY-MM-DD date or an empty string."""
    if not date_str or date_str.strip().lower() in MISSING_VALUES:
        return ""

    date_str = date_str.strip()

    for date_format in DATE_FORMATS:
        try:
            parsed_date = datetime.strptime(date_str, date_format)
            return parsed_date.strftime("%Y-%m-%d")
        except ValueError:
            continue

    return ""
