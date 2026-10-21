
from config import LOG_LEVELS
from services.analysis_service import analyze_logs
from services.log_parser import get_log_level


def view_logs(log_entries: list[str]) -> None:
    """Display all loaded log entries."""
    if not log_entries:
        print("\nNo log entries are currently loaded.")
        return

    print("\n--- Log File Preview ---")

    for number, entry in enumerate(log_entries, start=1):
        print(f"{number:>4}: {entry}")

    print(f"\nTotal entries: {len(log_entries)}")


def display_log_analysis(log_entries: list[str]) -> None:
    """Display log-level counts and error summaries."""
    counts = analyze_logs(log_entries)

    print("\n--- Log Analysis Report ---")
    print(f"Total entries: {len(log_entries)}")
    print("-" * 35)

    for level in LOG_LEVELS:
        print(f"{level:<10}: {counts.get(level, 0)}")

    unclassified = sum(
        1 for entry in log_entries if get_log_level(entry) is None
    )

    print(f"{'UNKNOWN':<10}: {unclassified}")
    print("-" * 35)
    print(
        "Errors and critical events: "
        f"{counts.get('ERROR', 0) + counts.get('CRITICAL', 0)}"
    )


def display_cleaning_report(
    original: list[str],
    cleaned: list[str],
) -> None:
    """Display cleaning statistics."""
    modified_count = sum(
        old != new for old, new in zip(original, cleaned)
    )

    print("\n--- Log Cleaning Results ---")
    print(f"Entries processed: {len(original)}")
    print(f"Entries modified: {modified_count}")


def display_validation_report(results: dict) -> None:
    """Display validation results."""
    invalid_levels = results["invalid_levels"]
    invalid_dates = results["invalid_dates"]

    print("\n--- Log Validation Report ---")
    print(f"Entries checked: {results['entries_checked']}")
    print(f"Entries with unrecognized levels: {len(invalid_levels)}")
    print(f"Entries with invalid dates: {len(invalid_dates)}")

    if invalid_levels:
        print(f"Missing/unrecognized levels on lines: {invalid_levels}")

    if invalid_dates:
        print(f"Invalid dates on lines: {invalid_dates}")

    if not invalid_levels and not invalid_dates:
        print("All entries passed the available validation checks.")


def display_missing_data_report(results: dict) -> None:
    """Display missing-data results."""
    empty_lines = results["empty_lines"]
    missing_levels = results["missing_levels"]

    print("\n--- Missing Data Report ---")
    print(f"Empty lines: {len(empty_lines)}")
    print(
        "Entries missing a recognized log level: "
        f"{len(missing_levels)}"
    )

    if empty_lines:
        print(f"Empty line numbers: {empty_lines}")

    if missing_levels:
        print(f"Unclassified line numbers: {missing_levels}")
